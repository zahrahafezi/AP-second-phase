from django import forms
from .models import Booking, DATE_CHOICES, TIME_CHOICES


class BookingForm(forms.ModelForm):
    date = forms.ChoiceField(choices=DATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'doctor', 'clinic', 'Disease', 'status']

