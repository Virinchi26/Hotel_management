from django.shortcuts import render
from django.http import HttpResponse
from .models import Location,Room
from django.core.paginator import Paginator
# hotel_management/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

import stripe
from django.conf import settings
from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import LoginForm


# Create your views here.
def index(request):
    locs = Location.objects.all()
    return render(request,'index.html',{'locs':locs} )

def about(request):
    
    return render(request,'about.html')


def room_detail(request):
    
    return render(request,'room_detail.html')


def rooms(request):
    if request.method == 'POST':
        # Token is created using Checkout or Elements!
        # Get the payment token ID submitted by the form:
        roomheater = False
        ac = False
        wifi = False
        tv = False
        adults = -1
        rooms = Room.objects.all()
        if 'roomheater' in request.POST:
            roomheater = True
            print(request.POST['roomheater'])
            rooms = rooms.filter(room_heater=True)
        if 'ac' in request.POST:
            ac = True
            rooms = rooms.filter(ac=True)
        if 'wifi' in request.POST:
            wifi = True
            rooms = rooms.filter(wifi=True)
        if 'tv' in request.POST:
            tv = True
            rooms = rooms.filter(tv=True)
        page = request.GET.get('page')
        location_query = request.GET.get('location','')
        if location_query:
            # Filter rooms based on the location query
            rooms = rooms.filter(location__icontains=location_query)
        
        items_per_page = 4  # You can adjust this to your preference

        paginator = Paginator(rooms, items_per_page)
        page_number = page
        page_obj = paginator.get_page(page_number)

        return render(request, 'rooms.html', {'roomheater': roomheater, 'ac': ac, 'wifi': wifi, 'tv':tv, 'rooms': rooms,'room_page': page_obj , 'location_query': location_query})
    page = request.GET.get('page')
    rooms = Room.objects.all()
    location_query = request.GET.get('location','')
    if location_query:
        # Filter rooms based on the location query
        rooms = rooms.filter(location__icontains=location_query)
    
    items_per_page = 4  # You can adjust this to your preference

    paginator = Paginator(rooms, items_per_page)
    page_number = page
    page_obj = paginator.get_page(page_number)

    return render(request, 'rooms.html', {'rooms': rooms,'room_page': page_obj , 'location_query': location_query})

def facilities(request):
    return render(request,'facilities.html')

def contactus(request):
    return render(request,'contactus.html')


stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request):
    if request.method == 'POST':
        # Token is created using Checkout or Elements!
        # Get the payment token ID submitted by the form:
        token = request.POST['stripeToken'] # Using Flask

        # Charge the user's card:
        charge = stripe.Charge.create(
            amount=1000,  # Amount in cents
            currency='usd',
            description='Hotel booking payment',
            source=token,
        )

        # You can save the charge information in your database here.

        return render(request, 'payment_success.html')
    
    return render(request, 'payment_form.html', {'stripe_public_key': settings.STRIPE_PUBLIC_KEY})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')

from .forms import SignupForm

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(username=username, email=email, password=password)
                    auth.login(request, user)
                    return redirect('/')
                else:
                    form.add_error('username', 'Username is already taken.')
            else:
                form.add_error('confirm_password', 'Passwords do not match.')
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})

    