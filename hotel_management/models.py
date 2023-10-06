from django.db import models

# Create your models here.
# class Location(models.Model):
#     id: int
#     name: str
#     img: str

class Location(models.Model):
    name= models.CharField(max_length=100)
    desc= models.TextField()
    img= models.ImageField(upload_to='pics') #folder name pics will be created in media folder