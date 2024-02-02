from django.shortcuts import render, redirect
from .forms import BookingForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def book_appointment(request):
    # this is the book_appointment view that shows the booking form of the app
    # check if the user is logged in and is a patient
    if request.user.is_authenticated and request.user.userrole.role == 'patient':
        # if the request type is POST
        if request.method == 'POST':
            # create an object from the booking form with the request data
            form = BookingForm(request.POST)
            # check the validity of the form
            if form.is_valid():
                # save the booking in the database
                form.save()
                # redirect to the confirmation page
                return redirect('confirmation')
        # if the request type is GET
        else:
            # create an empty booking form object
            form = BookingForm()
        # rendering
        return render(request, 'book_appointment.html', {'form': form})
    else:
        # redirect to the login page
        return redirect('login')
