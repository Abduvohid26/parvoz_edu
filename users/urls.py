from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.LoginAPIView.as_view()),
    path('register/', views.RegisterAPIView.as_view()),
]
