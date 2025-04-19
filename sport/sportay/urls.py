from django.urls import path
from .views import RegisterView, index, booking_list, BookingView
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view(template_name='users/login.html')),
    path('', index, name='base'),
    path('booking_list/', booking_list, name='booking_list'),
    path('booking/', BookingView.as_view()),
]
