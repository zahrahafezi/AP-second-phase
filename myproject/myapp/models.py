from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Userrole(User):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('secretary', 'Secretary'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
