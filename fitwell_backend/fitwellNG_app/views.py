from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomUserCreationForm
from .models import User
import requests
from django.contrib.auth.decorators import login_required


def home(request):
    videoList = getVideos()
    print(videoList)
    return render(request, 'index.html', {'videoList': videoList})
    # return render(request, 'landing.html')


def about(request):
    return render(request, 'about.html')

@login_required(redirect_field_name='dashboard', login_url='/login')
def dashboard(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    if(request.user.is_authenticated):
        return redirect('/dashboard')
    errors = ""
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            errors = "Login Failed! Wrong username or password"
    return render(request, 'Registration/login.html', {"errors": errors})


def is_valid(data):
    errors = []

    # Validate First name and Last name
    if data['f_name'] == "" or data["l_name"] == "":
        errors.append("First Name and Last name are required!")
    # validate email:
    email = data['email']

    if str(email) == "":
        errors.append('Email Field is required.')
    elif str(email).__contains__("@") is False:
        errors.append(f'Email Address "{str(email)}" is not valid.')

    # validate password
    # =====================
    pass1 = data['password']

    if pass1 == "":
        errors.append('Password Field is Required.')
    elif len(pass1) < 8:
        errors.append('Password should not be less than 8 characters.')

    if len(errors) > 0:
      return errors

    if len(errors) == 0:
        return None


def sign_up(request):
    if(request.user.is_authenticated):
        return redirect('/dashboard')
    if request.method == 'POST':
        data = request.POST
        errors = is_valid(data)
        if errors is None:
            try:
                newUser = User.objects.create_user(email=data['email'],
                                                   password=data['password'],
                                                   first_name=data['f_name'],
                                                   last_name=data['l_name'],
                                                   height=data['height'],
                                                   weight=data['weight'],
                                                   phone_number=data['phone'])

                newUser.save()
            except Exception as e:
                # check for email address issue
                if str(e).lower() == 'UNIQUE constraint failed: fitwellNG_app_user.email'.lower() or str(e).lower().__contains__('duplicate key value violates unique constraint'):
                    m = f"User with Email Address ' {data['email']} ' already exists. Please choose another Email Address"
                    return render(request, 'Registration/sign-up.html', {'errors': [m]})
                elif str(e).lower().__contains__("value must be a decimal number"):
                    m = "Please specify a value for 'Weight' and 'Height' "
                    return render(request, 'Registration/sign-up.html', {'errors': [m]})

                else:
                    return render(request, 'Registration/sign-up.html', {'errors': [f'\n{e}']})

            return redirect('/login')
        else:
            return render(request, 'Registration/sign-up.html', {'errors': errors})

    return render(request, 'Registration/sign-up.html')


class Video():
    def __init__(self, image, videoId):
        self.image = image
        self.videoId = videoId


def getVideos():
    r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=6&playlistId=PLI37FJmOtrj32rGK4zPL3Cpr9v28uLQL9&key=AIzaSyBrGMILVCYBO4xMmaO0DHqxhZDD-ozonjA')
    videos = r.json()
    videoList = [Video(video['snippet']['thumbnails']['high']['url'], video['snippet']['resourceId']['videoId'])
                 for video in videos['items'] if video['snippet']['resourceId']['kind'] == "youtube#video"]
    return videoList
