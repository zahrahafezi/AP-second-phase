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
# def booking(request):
#     if request.method == 'POST':
#         clinic = request.POST.get('clinic')
#         day = request.POST.get('day')
#         hour = request.POST.get('hour')
#         if clinic == None:
#             messages.success(request, "Please Select A clinic!")
#             return redirect('user_booking')
#         if day == None:
#             messages.success(request, "Please Select A day!")
#             return redirect('user_booking')
#         if hour == None:
#             messages.success(request, "Please Select A hour!")
#             return redirect('user_booking')
#     return redirect('user_booking')

# update taken times for that clinic in database:
# for the next time, don't show taken hours of that day for that clinic


def booking(request):
    return render(request, 'user_booking.html')


def profile_patient(request):
    return render(request, 'profile_patient.html')


def profile_secretary(request):
    return render(request, 'profile_secretary.html')


def calendar_secretary(request):
    return render(request, 'calendar_secretary.html')


def calendar_patient(request):
    return render(request, 'calendar_patient.html')


