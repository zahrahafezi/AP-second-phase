from django.urls import path
from . import views

urlpatterns = [
    path('book_appointment/', views.book_appointment, name='book_appointment'),
]
