from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':  #fetch the data and check
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password) #check the user is valid or not
        # if user is valid then user is not None
        # if the same user name and password exists then it will give user object

        if user is not None: #wrong username and password
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html') #not post request


def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken') # messages.info is used to print in html
                # print('username taken')  print is used to print in terminal
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                # print('email taken')
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        
        else:
            # print('password not matching')
            messages.info(request,'Password not matching')
            return redirect('register')

        return redirect('/')
    else:
        return render(request, 'register.html')
