from django.urls import path
from . import views

urlpatterns = [
    path('user_booking/', views.booking, name='user_booking'),
    path('profile_patient/', views.profile_patient, name='profile_patient'),
    path('profile_secretary/', views.profile_secretary, name='profile_secretary'),
]
