from django import forms
<<<<<<< Updated upstream
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'doctor', 'clinic', 'Disease']
=======
from django.contrib.auth.forms import UserCreationForm


class ClinicCreation(UserCreationForm):
    ClinicName = forms.CharField(label='Clinic Name', max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    ClinicTimes = forms.CharField(label='Clinic Times', max_length=50,
                                  widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super(ClinicCreation, self).__init__(*args, **kwargs)
        self.fields['ClinicName'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['ClinicTimes'].widget.attrs['class'] = 'form-control form-control-lg'
>>>>>>> Stashed changes
