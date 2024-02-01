from django.db import models

from django.db import models


class Users(models.Model):
    name = models.TextField()
    email = models.EmailField(unique=True)
    user_type = models.TextField()
    password = models.TextField()


class Rating(models.Model):
    clinic = models.OneToOneField('Clinics', primary_key=True, on_delete=models.CASCADE)
    rate = models.TextField()
    opinion = models.TextField()


class MedicationRecord(models.Model):
    user = models.OneToOneField(Users, primary_key=True, on_delete=models.CASCADE)
    clinic = models.ForeignKey('Clinics', on_delete=models.CASCADE)
    name_medicine = models.TextField()
    medicine_id = models.TextField()
    status = models.TextField()
    instructions = models.TextField()


class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    clinic_name = models.TextField()
    datetime = models.TextField()
    status = models.TextField()


class Clinics(models.Model):
    name = models.TextField()
    contact_number = models.TextField()
    address = models.TextField()
    email = models.EmailField()
    availability = models.TextField()
    services = models.TextField()
    reserve_slot = models.TextField()
