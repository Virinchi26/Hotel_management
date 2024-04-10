from .models import Location, Room, Booking
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import LoginForm
from datetime import datetime, timedelta
from .forms import ContactForm
from django.http import JsonResponse


# Create your views here.
def index(request):
    locs = Location.objects.all()
    return render(request, "index.html", {"locs": locs})


def about(request):
    return render(request, "about.html")


def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "profile.html", {"bookings": bookings})



def room_detail(request, id):
    room = Room.objects.get(pk=int(id))
    bookings = Booking.objects.filter(room=room)
    booked_dates = []
    for booking in bookings:
        checkin = booking.checkin
        checkout = booking.checkout
        delta = checkout - checkin
        for i in range(delta.days + 1):
            day = checkin + timedelta(days=i)
            booked_dates.append(day.strftime("%Y-%m-%d"))
    print(booked_dates)
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            s = request.POST["daterange"]
            checkin, checkout = s.split(" - ")
            checkin = checkin.strip()
            checkout = checkout.strip()
            checkin = datetime.strptime(checkin, "%m/%d/%Y").date()
            checkout = datetime.strptime(checkout, "%m/%d/%Y").date()
            adults = request.POST["adults"]
            children = request.POST["children"]
            room = Room.objects.get(pk=int(id))
            booking = Booking.objects.create(
                user=user,
                room=room,
                checkin=checkin,
                checkout=checkout,
                adults=adults,
                children=children,
            )
            print(booking)
            booking.save()
            # return redirect('index')
        else:
            return redirect("login")
    booking.save()
    return render(request, "room_detail.html", {"room": room, "booked_dates": booked_dates})



def rooms(request):
    if request.method == "POST":
        # Token is created using Checkout or Elements!
        # Get the payment token ID submitted by the form
        roomheater = False
        ac = False
        wifi = False
        tv = False
        adults = -1
        rooms = Room.objects.all()
        if "roomheater" in request.POST:
            roomheater = True
            print(request.POST["roomheater"])
            rooms = rooms.filter(room_heater=True)
        if "ac" in request.POST:
            ac = True
            rooms = rooms.filter(ac=True)
        if "wifi" in request.POST:
            wifi = True
            rooms = rooms.filter(wifi=True)
        if "tv" in request.POST:
            tv = True
            rooms = rooms.filter(tv=True)
        page = request.GET.get("page")
        location_query = request.GET.get("location", "")
        if location_query:
            # Filter rooms based on the location query
            rooms = rooms.filter(location__icontains=location_query)

        items_per_page = 4  # You can adjust this to your preference

        paginator = Paginator(rooms, items_per_page)
        page_number = page
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "rooms.html",
            {
                "roomheater": roomheater,
                "ac": ac,
                "wifi": wifi,
                "tv": tv,
                "rooms": rooms,
                "room_page": page_obj,
                "location_query": location_query,
            },
        )
    page = request.GET.get("page")
    rooms = Room.objects.all()
    location_query = request.GET.get("location", "")
    if location_query:
        # Filter rooms based on the location query
        rooms = rooms.filter(location__icontains=location_query)

    items_per_page = 4  # You can adjust this to your preference

    paginator = Paginator(rooms, items_per_page)
    page_number = page
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "rooms.html",
        {"rooms": rooms, "room_page": page_obj, "location_query": location_query},
    )


def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "profile.html", {"bookings": bookings})


def facilities(request):
    return render(request, "facilities.html")


def contactus(request):
    form_submitted = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent successfully!")
            form_submitted = True
            form = ContactForm()  # Create a new, empty form instance
    else:
        form = ContactForm()

    return render(
        request, "contactus.html", {"form": form, "form_submitted": form_submitted}
    )


from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login as auth_login

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(
                    None, "Invalid username or password."
                )  # Adding non-field error
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout(request):
    auth.logout(request)
    return redirect("/")


from .forms import SignupForm

from django.contrib.auth import login as auth_login


def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

            if password == confirm_password:
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(
                        username=username, email=email, password=password
                    )
                    auth_login(
                        request,
                        user,
                        backend="django.contrib.auth.backends.ModelBackend",
                    )
                    return redirect("/")
                else:
                    form.add_error("username", "Username is already taken.")
            else:
                form.add_error("confirm_password", "Passwords do not match.")
    else:
        form = SignupForm()

    return render(request, "register.html", {"form": form})

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_bill(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    template_path = 'bill_template.html'
    context = {'booking': booking}
    # Render the template
    template = get_template(template_path)
    html = template.render(context)
    # Create a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="bill.pdf"'  # Use 'inline' to display in browser
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

# def download_bill(request, booking_id):
#     booking = Booking.objects.get(id=booking_id)
#     template_path = 'bill_template.html'
#     context = {'booking': booking}
#     # Render the template
#     template = get_template(template_path)
#     html = template.render(context)
#     # Create a PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="bill.pdf"'
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

