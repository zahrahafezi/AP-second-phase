from django.contrib import admin

from .models import Booking

# ثبت مدل Booking در پنل ادمین
admin.site.register(Booking)