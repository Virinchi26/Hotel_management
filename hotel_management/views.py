from django.shortcuts import render
from django.http import HttpResponse
from .models import Location
# Create your views here.
def index(request):
    # static content
    # loc1 = Location()
    # loc1.name = 'Goa'
    # loc1.desc = 'Beutiful beaches'
    # loc1.img = 'destination_1.jpg'

    # loc2 = Location()
    # loc2.name = 'Mumbai' 
    # loc2.desc = 'The City That Never Sleeps'
    # loc2.img = 'destination_2.jpg'

    # loc3 = Location()
    # loc3.name = 'Delhi'
    # loc3.desc = 'Capital of India'
    # loc3.img = 'destination_3.jpg'

    # loc4 = Location()
    # loc4.name = 'Hyderabad'
    # loc4.desc = 'City of Pearls'
    # loc4.img = 'destination_4.jpg'

    # loc5 = Location()
    # loc5.name = 'Bangalore'
    # loc5.desc = 'Silicon Valley of India'
    # loc5.img = 'destination_5.jpg'

    # loc6 = Location()
    # loc6.name = 'Chennai'
    # loc6.desc = 'City of Temples'
    # loc6.img = 'destination_6.jpg'

    # locs = [loc1,loc2,loc3,loc4,loc5]
    locs = Location.objects.all()
    return render(request,'index.html',{'locs':locs} )

def about(request):
    return render(request,'about.html')

def rooms(request):
    return render(request,'rooms.html')

def facilities(request):
    return render(request,'facilities.html')

def contactus(request):
    return render(request,'contactus.html')
