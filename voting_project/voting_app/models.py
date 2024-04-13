from django.db import models

# Create your models here.
# voting_app/models.py

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Password should be hashed and salted
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


