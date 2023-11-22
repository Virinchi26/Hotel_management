from django.db import models

class Location(models.Model):
    name= models.CharField(max_length=100)
    desc= models.TextField()
    img= models.ImageField(upload_to='pics') #folder name pics will be created in media folder


class Room(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='pics')
    
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

    price_per_night = models.FloatField()


class AdditionalImage(models.Model):
    room = models.ForeignKey(Room, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='additional_images/')


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='pics')

class RoomRating(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.FloatField()

class UserReview(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    review = models.TextField()
    