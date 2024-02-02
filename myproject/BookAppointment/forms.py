from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'doctor', 'clinic', 'Disease']
