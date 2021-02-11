from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(('phone_number'), max_length=150, unique=True,
                    error_messages={'unique': ("A user with that phone number already exists.")})

