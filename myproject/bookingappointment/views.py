from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.shortcuts import render, get_object_or_404
from .models import Booking


@login_required
def book_appointment(request):
    if request.user.is_authenticated and request.user.userrole.role == 'patient':
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.patient_id = request.user.id
                booking.save()
                return redirect('confirmation', pk=booking.pk)  # Pass booking id as parameter
        else:
            form = BookingForm()
        return render(request, 'book_appointment.html', {'form': form})
    else:
        return redirect('login')


def confirmation(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'confirmation.html', {'booking': booking})


def user_appointments(request):
    # اطلاعات بیماران جاری را از پایگاه داده استخراج کنید
    appointments = Booking.objects.filter(patient=request.user)
    return render(request, 'user_appointments.html', {'appointments': appointments})


def receptionist_dashboard(request):
    # دریافت همه‌ی نوبت‌ها از پایگاه داده
    appointments = Booking.objects.filter(patient=request.user)

    # ارسال لیست نوبت‌ها به تمپلیت
    return render(request, 'receptionist_dashboard.html', {'appointments': appointments})



