from django.shortcuts import redirect, render
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# pages:
# index(log out option)
# sign_up
# log_in
# index_staff(calendar, user panel)
### update_profile staff
### Update_Clinic_Info staff
# index_patient(online booking, calendar, user panel)
### update_profile patient


# for staff:
### update_profile (need a page for it. Through user panel.)
# view_appointment (in calendar page)
### Update_Clinic_Info (need a page for it. Through user panel)
# cancel_appointment (in calendar page.)

# for user:
# view_appointment (in calendar page)
### update_profile (need a page for it. Through user panel.)
# book_appointment (user booking page)
# cancel_appointment (in calendar page.)
### update_booking_time (redirect to user booking page but with the same clinic.)


# user_booking
def booking(request):
    if request.method == 'POST':
        clinic = request.POST.get('clinic')
        day = request.POST.get('day')
        hour = request.POST.get('hour')
        if clinic == None:
            messages.success(request, "Please Select A clinic!")
            return redirect('booking')
        if day == None:
            messages.success(request, "Please Select A day!")
            return redirect('booking')
        if hour == None:
            messages.success(request, "Please Select A hour!")
            return redirect('booking')

        # update taken times for that clinic in database:
        # for the next time, don't show taken hours of that day for that clinic


@login_required
def staff_home(request):
    # Check if the user's role is staff
    if request.user.profile.role == 'staff':
        return render(request, 'staff_home.html')
    else:
        # Redirect to a different page if the user is not staff
        return redirect('home')


def patient_home(request):
    pass
