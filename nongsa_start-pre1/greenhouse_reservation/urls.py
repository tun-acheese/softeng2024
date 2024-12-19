# calendar_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.reservation_view, name='reservation_view'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
]
