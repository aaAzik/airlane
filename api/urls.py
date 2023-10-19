from django.urls import path
from .views import *

urlpatterns = [
    path('airlane/', AirlaneAPIView.as_view()),
    path('airlane/<int:pk>/', AirlaneDetailAPiView.as_view()),
    path('plane/', PlaneAPIView.as_view()),
    path('plane/<int:pk>/', PlaneDetailAPiView.as_view()),
    path('flight/', FlightAPIView.as_view()),
    path('flight/<int:pk>/', FlightDetailAPiView.as_view()),
    ]