from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    PUBLISHER = 'PUBLISHER'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (PUBLISHER, 'Publisher'),
        (SUBSCRIBER, 'Subscriber')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    email = models.fields.EmailField(unique=True)
    username = None
    profile_picture = models.ImageField(null=True)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now=True)
