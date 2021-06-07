from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]