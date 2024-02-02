from django.urls import path
from . import views

urlpatterns = [
    path('user_booking/', views.booking, name='user_booking'),
    path('profile_patient/', views.profile_patient, name='profile_patient'),
    path('profile_secretary/', views.profile_secretary, name='profile_secretary'),
path('calendar_patient/', views.calendar_patient, name='calendar_patient'),
path('calendar_secretary/', views.calendar_secretary, name='calendar_secretary'),
]
