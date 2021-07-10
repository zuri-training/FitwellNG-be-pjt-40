from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomUserCreationForm, PlanSubscriptionForm
from .models import User, MealPlans, WorkoutPlan, WorkoutPlanList
from django.views.generic import UpdateView, ListView
import requests
from django.contrib.auth.decorators import login_required


class update_user(UpdateView):

    model = User
    fields = ['first_name', 'nationality', 'sex', 'dob', 'state', 'image']
    success_url = '/'
    template_name = "update.html"


class Plans(ListView):
    template_name = "plans.html"
    model = WorkoutPlan


def plans(request):
    return render(request, 'plans.html')


def home(request):
    # getUserData('jbadonai@gmail.com', 'afolayemi')
    # getUserData('jayadonai@yahoo.com', 'afolayemi')
    videoList = getVideos()
    # print(videoList)
    return render(request, 'index.html', {'videoList': videoList})
    # return render(request, 'landing.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    if request.method == "POST":
        print(f"User: {request.user.pk}")
        print(request.POST)
        form  = PlanSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            print("saveddddddddddddd")

    form = PlanSubscriptionForm()
    meal = MealPlans.objects.all()
    workouts = WorkoutPlan.objects.all()
    workout_list = WorkoutPlanList.objects.all()

    return render(request, 'dashboard.html', {'workout_list': workout_list, 'form':form})


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    message = ""
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            message = "Login Failed! Wrong username or password"
    return render(request, 'login.html', {"message": message})


def is_valid(data):
    message = []

    # Validate First name and Last name
    if data['first_name'] == "" or data["last_name"] == "":
        message.append(('name', "First Name and Last name are required!"))
    # validate email:
    email = data['email']

    if str(email) == "":
        message.append(('email', 'Email Field is required.'))
    elif str(email).__contains__("@") is False:
        message.append(('email', f'Email Address "{str(email)}" is not valid.'))

    # validate password
    #=====================
    pass1 = data['password']
    # pass2 = data['password2']
    #
    # if pass1 == "" or pass2 == "":
    #     message.append(('password', 'Password Field is Required.'))
    if len(pass1) < 8:
        message.append(('password', 'Password should not be less than 8 characters.'))
    # elif pass1 != pass2:
    #     message.append(('password', 'Passwords do not match.'))

    # validate security question
    # if data['security'] == "" or data['security_answer'] == "":
    #     message.append(('security', 'Security Question and answer are required.'))
    #
    # # validate date of birth
    # if data['dob'] == "":
    #     message.append(('Date of Birth', "Date of Birth is Required."))

    newdata = ""
    if len(message)> 0:
        if len(message) > 1:
            for index, m in enumerate(message, start=1):
                d = f"{index}. {m[1]}"
                newdata += f"{d}<br>"

            newdata = f"Signup not successful!. <br><br> {newdata}" \
                f"<br><br> Please provide all the required information above and try again"

        if len(message) == 1:
            for index, m in enumerate(message, start=1):
                d = f"{index}. &nbsp; &nbsp; {m[1]}"
                newdata += f"{d}<br>"

            newdata = f"Sign up not successful:<br><br> {newdata}"

    if len(message) == 0:
        return None
    else:

        return newdata


def sign_up(request):
    if request.method == 'POST':
        data = request.POST
        ans = is_valid(data)
        if ans is None:
            try:
                newUser = User.objects.create_user(email=data['email'],
                                                   password=data['password'],
                                                   first_name=data['first_name'],
                                                   last_name=data['last_name'],
                                                   # dob=data['dob'],
                                                   # sex=data['sex'],
                                                   # nationality=data['nationality'],
                                                   # state=data['state'],
                                                   height=data['height'],
                                                   weight=data['weight'],
                                                   # security=data['security'],
                                                   phone_no=data['phone_no'])

                newUser.save()
            except Exception as e:
                # check for email address issue
                if str(e).lower() == 'UNIQUE constraint failed: fitwellNG_app_user.email'.lower() or str(e).lower().__contains__('duplicate key value violates unique constraint'):
                    m = f"User with Email Address ' {data['email']} ' already exists. Please choose another Email Address"
                    return render(request, 'sign-up.html', {'message': m , 'data': data})
                elif str(e).lower().__contains__("value must be a decimal number"):
                    m = "<b>Error: </b><br><br>Please specify a value for 'Weight' and 'Height' "
                    return render(request, 'sign-up.html', {'message': m})

                else:
                    return render(request, 'sign-up.html', {'message': f'\n{e}'})

            return render(request, 'signup_success.html', {'data': data})
            # return redirect('/sign-up')
            # return redirect('/login')
        else:
            return render(request, 'sign-up.html', {'message': ans, 'data':data})

    # return render(request, 'signup_success.html')
    return render(request, 'sign-up.html')


def sign_up1(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        print("form data:::::")

        print(form.data)
        # print(form.cleaned_data)
        print(form.data['password1'] == form.data['password2'])
        print(form.error_messages)
        if form.is_valid():
            print(f"[][] form is valid")

            form.save()
            # email = request.POST['email']
            # password = request.POST['password1']
            # user = authenticate(email=email, password=password)
            # if user is not None:
            #     login(request, user)
            return redirect('/')
        else:
            print('<><> form is not valid')
            print(form.error_messages)
            return  redirect('sign-up')
    else:

        # print(f"[][] here [][] {form._post_clean()}")

        return render(request, 'sign-up.html', {'form': form})

    # return render(request, 'sign-up.html', {'form': form})

class Video():
    def __init__(self, image, videoId):
        self.image = image
        self.videoId = videoId

def getVideos():
    r = requests.get('https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=6&playlistId=PLI37FJmOtrj32rGK4zPL3Cpr9v28uLQL9&key=AIzaSyBrGMILVCYBO4xMmaO0DHqxhZDD-ozonjA')
    videos = r.json()
    videoList = [Video(video['snippet']['thumbnails']['high']['url'], video['snippet']['resourceId']['videoId']) for video in videos['items'] if video['snippet']['resourceId']['kind'] == "youtube#video"]
    return videoList


def getUserData(username, password):
    # # get token
    # r = requests.post('http://127.0.0.1:8000/api/users/get-token/', data={'username': username, 'password': password})
    # token = r.json()['token']
    #
    # # get details based using the token above
    # r2 = requests.get('http://127.0.0.1:8000/api/users/', headers={"Authorization": f"Token {token}"})

    # create
    r3 = requests.post('http://127.0.0.1:8000/api/users/create/', data={'username': username, 'password': password})

    print(f"[][]{r3.status_code}")