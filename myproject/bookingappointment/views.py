from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


@login_required
def book_appointment(request):
    if request.user.is_authenticated and request.user.userrole.role == 'patient':
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('confirmation')
        else:
            form = BookingForm()
        return render(request, 'book_appointment.html', {'form': form})
    else:
        return redirect('login')

