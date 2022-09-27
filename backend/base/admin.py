from django.contrib import admin

# Register your models here.
from .models import  Notes, Subscription

admin.site.register(Notes)
admin.site.register(Subscription)