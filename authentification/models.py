from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    PUBLISHER = 'PUBLISHER'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (PUBLISHER, 'Publisher'),
        (SUBSCRIBER, 'Subscriber')
    )

    email = models.fields.EmailField(unique=True)
    username = models.fields.CharField(unique=True, null=True, max_length=128)
    profile_picture = models.ImageField(null=True)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now=True)
