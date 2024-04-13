from django.contrib import admin

# Register your models here.

# voting_app/admin.py

from django.contrib import admin
from .models import ContactMessage, User

admin.site.register(ContactMessage)
admin.site.register(User)

