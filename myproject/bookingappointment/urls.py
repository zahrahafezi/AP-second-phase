from django.urls import path
from . import views

urlpatterns = [
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('confirmation/<int:pk>/', views.confirmation, name='confirmation'),
    path('user_appointments/', views.user_appointments, name='user_appointments'),
]
