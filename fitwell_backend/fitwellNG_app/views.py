from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomUserCreationForm
from .models import User

def home(request):
    return render(request, 'index.html')
    # return render(request, 'landing.html')


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
    pass1 = data['password1']
    pass2 = data['password2']

    if pass1 == "" or pass2 == "":
        message.append(('password', 'Password Field is Required.'))
    elif len(pass1) < 8 or len(pass2) < 8:
        message.append(('password', 'Password should not be less than 8 characters.'))
    elif pass1 != pass2:
        message.append(('password', 'Passwords do not match.'))

    # validate security question
    if data['security'] == "" or data['security_answer'] == "":
        message.append(('security', 'Security Question and answer are required.'))

    # validate date of birth
    if data['dob'] == "":
        message.append(('Date of Birth', "Date of Birth is Required."))

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

            newdata = f"Signup Failed due to the error below <br><br> {newdata}" \
                f"<br><br> Please provide the required information above and try again"

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
                                                   password=data['password1'],
                                                   first_name=data['first_name'],
                                                   last_name=data['last_name'],
                                                   dob=data['dob'],
                                                   sex=data['sex'],
                                                   nationality=data['nationality'],
                                                   state=data['state'],
                                                   height=data['height'],
                                                   weight=data['weight'],
                                                   security=data['security'],
                                                   security_answer=data['security_answer'])

                newUser.save()
            except Exception as e:
                # check for email address issue
                if str(e).lower() == 'UNIQUE constraint failed: fitwellNG_app_user.email'.lower() or str(e).lower().__contains__('duplicate key value violates unique constraint'):
                    m = f"<b>Error:</b> <br> User with Email Address ' {data['email']} ' already exists. Please choose another Email Address"
                    return render(request, 'sign-up.html', {'message': m })
                elif str(e).lower().__contains__("value must be a decimal number"):
                    m = "<b>Error: </b><br><br>Please specify a value for 'Weight' and 'Height' "
                    return render(request, 'sign-up.html', {'message': m})

                else:
                    return render(request, 'sign-up.html', {'message': f'\n{e}'})

            # return render(request, 'login.html', {'message': "Sign up successful"})
            return redirect('/login')
        else:
            return render(request, 'sign-up.html', {'message': ans})

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



