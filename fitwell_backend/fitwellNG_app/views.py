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
    # validate email:
    email = data['email']
    if str(email).__contains__("@") is False:
        message.append(('email', 'Invalid email address.'))

    # validate password
    pass1 = data['password1']
    pass2 = data['password2']


    if pass1 != pass2 or pass1 == "" or pass2 == "" or len(pass1) != len(pass1):
        message.append(('password', 'Password do not match.'))

    # validate security question
    if data['security'] == "" or data['security_answer'] == "":
        message.append(('security', 'Security Question and answer required.'))

    # validate date of birth
    if data['dob'] == "":
        message.append(('Date of Birth', "Date of Birth is Required."))

    newdata = ""
    if len(message)> 0:
        if len(message) > 1:
            for index, m in enumerate(message, start=1):
                d = f"{index}. {m[1]}"
                newdata += f"{d}<br>"

            newdata = f"Signup Failed due to the errors below <br><br> {newdata}" \
                f"<br><br> Please provide all the required information above and try again"

        if len(message) == 1:
            for index, m in enumerate(message, start=1):
                d = f"{index}. {m[1]}"
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
                if str(e).lower() == 'UNIQUE constraint failed: fitwellNG_app_user.email'.lower():
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



