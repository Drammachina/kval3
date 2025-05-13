from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name= 'телефон')
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone']
    USERNAME_FIELD = 'username'

class Cart(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    img = models.ImageField(upload_to='img/')