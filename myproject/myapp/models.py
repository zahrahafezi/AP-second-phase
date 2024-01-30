from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# تعریف یک مدل کاربر از نوع AbstractUser
class Userrole(User):
    # تعریف یک فیلد به نام role که می‌تواند دو مقدار patient یا secretary را بگیرد
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('secretary', 'Secretary'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
