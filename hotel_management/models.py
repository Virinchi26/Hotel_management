from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name= models.CharField(max_length=100)
    desc= models.TextField()
    img= models.ImageField(upload_to='pics') #folder name pics will be created in media folder

class Images(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=255)
    images = models.ManyToManyField(Images)
    
    # features
    rooms = models.IntegerField() 
    bathrooms = models.IntegerField() 
    balcony = models.IntegerField() 
    sofa = models.IntegerField() 

    # facilities
    room_heater = models.BooleanField()
    ac = models.BooleanField()
    wifi = models.BooleanField()
    tv = models.BooleanField()

    # guests
    adults = models.IntegerField()
    children = models.IntegerField()

    location = models.CharField(max_length=255)
    rating = models.FloatField()
    price_per_night = models.FloatField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.room.name + " - " + self.user.username + " - " + str(self.checkin) + " - " + str(self.checkout)




class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
