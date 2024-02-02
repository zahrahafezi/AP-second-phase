from django import forms
from .models import Booking  # import the Booking model from the app


class BookingForm(forms.Form):
    # inherit the fields from the Booking model
    class Meta:
        model = Booking
        fields = ['date', 'time', 'doctor', 'reason']
        widgets = {
            'time': forms.RadioSelect()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # get the selected date from the form
        date = self.data.get('date')
        # if the date is valid
        if date:
            # get the available time slots for the date
            available_times = Booking.get_available_times(date)
            # set the choices for the time field
            self.fields['time'].choices = [(t, t.strftime('%H:%M')) for t in available_times]