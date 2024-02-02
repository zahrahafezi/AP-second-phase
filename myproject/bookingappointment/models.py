from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    # one-to-many relation with the User model
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    # booking fields
    date = models.DateField()
    time = models.TimeField()
    doctor = models.CharField(max_length=50)
    reason = models.CharField(max_length=200)

    @classmethod
    def get_available_times(cls, date):
        # get the booked time slots for the date
        booked_times = cls.objects.filter(date=date).values_list('time', flat=True)
        # get the possible time slots from 8 AM to 4 PM with 30 minutes interval
        possible_times = [datetime.time(hour=h, minute=m) for h in range(8, 17) for m in (0, 30)]
        # return the difference between the possible and booked time slots
        return list(set(possible_times) - set(booked_times))
