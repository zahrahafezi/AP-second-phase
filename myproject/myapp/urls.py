from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('patient/', views.patient, name='patient'),  # new
    path('secretary/', views.secretary, name='secretary'),  # new
]

# TODO چرا در اندکس اچ تی ام ال وارد صفحه اصلی میشه و لاگ اوت و دیگه چیزی نی
