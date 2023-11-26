from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Images)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Location)
admin.site.register(ContactMessage)