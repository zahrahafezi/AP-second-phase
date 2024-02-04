from django.db import models
from django.contrib.auth.models import User

TIME_CHOICES = [
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00')
]
DATE_CHOICES = [
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday')
]
CLINIC_CHOICES = [
    ('Health Plus Clinic', 'Health Plus Clinic'),
    ('Care Wellness Center', 'Care Wellness Center'),
    ('Harmony Medical Group', 'Harmony Medical Group'),
    ('Vitality Clinic', 'Vitality Clinic'),
    ('Wellness Solutions Center', 'Wellness Solutions Center'),
    ('Heartland Family Health', 'Heartland Family Health'),
    ('Precision Dental Care', 'Precision Dental Care'),
    ('Radiant Skin Clinic', 'Radiant Skin Clinic')
]
DOCTOR_CHOICES = [
    ('Dr. Emily Johnson', 'Dr. Emily Johnson'),
    ('Dr. Michael Smith', 'Dr. Michael Smith'),
    ('Dr. Sarah Davis', 'Dr. Sarah Davis'),
    ('Dr. Robert Anderson', 'Dr. Robert Anderson'),
    ('Dr. Jessica White', 'Dr. Jessica White'),
    ('Dr. Brian Miller', 'Dr. Brian Miller'),
    ('Dr. Jennifer Brown', 'Dr. Jennifer Brown'),
    ('Dr. Christopher Lee', 'Dr. Christopher Lee')
]


class Booking(models.Model):
    STATUS_CHOICES = (
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='booked')
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50, choices=DATE_CHOICES)
    time = models.CharField(max_length=50, choices=TIME_CHOICES)
    clinic = models.CharField(max_length=50, choices=CLINIC_CHOICES)
    doctor = models.CharField(max_length=50, choices=DOCTOR_CHOICES)
    Disease = models.CharField(max_length=50)

