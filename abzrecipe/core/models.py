from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    phone = models.TextField(max_length=15, blank=True)
    address = models.TextField(max_length=250, blank=True)
    country = models.TextField(max_length=250, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=1050)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name