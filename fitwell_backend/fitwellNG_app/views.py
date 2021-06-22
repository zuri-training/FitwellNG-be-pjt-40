from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import User

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    return render(request, 'dashboard.html')


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
            return redirect('/')
        else:
            message = "Login Failed!"
    return render(request, 'login.html', {"message": message})


def is_valid(data):
    message = []
    # validate email:
    email = data['email_address']
    if str(email).__contains__("@") is False:
        message.append(('email', 'Invalid email address'))

    # validate password
    pass1 = data['pword1']
    pass2 = data['pword2']

    if pass1 != pass2 or pass1 == "" or pass2 == "":
        message.append(('password', 'Password do not match'))

    # validate security question
    if data['security_question'] == "" or data['security_answer'] == "":
        message.append(('security', 'Security Question and answer required.'))

    # validate date of birth
    if data['dob'] == "":
        message.append(('Date of Birth', "Date of Birth is Required."))

    newdata = ""
    if len(message)> 0:
        for index, m in enumerate(message, start=1):
            d = f"{index}. [{m[0]}]: {m[1]}"
            newdata += f"{d}\n\n"

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
                newUser = User.objects.create_user(email=data['email_address'],
                                                   password=data['pword1'],
                                                   first_name=data['first_name'],
                                                   last_name=data['last_name'],
                                                   dob=data['dob'],
                                                   sex=data['sex'],
                                                   nationality=data['nationality'],
                                                   state=data['state'],
                                                   height=data['height'],
                                                   weight=data['weight'],
                                                   security=data['security_question'],
                                                   security_answer=data['security_answer'])

                newUser.save()
            except Exception as e:
                return render(request, 'sign-up.html', {'message': 'Error! User with email address already exists, Please choose another email address'})

            # return render(request, 'login.html', {'message': "Sign up successful"})
            return redirect('/login')
        else:
            return render(request, 'sign-up.html', {'message': ans})

    return render(request, 'sign-up.html')


