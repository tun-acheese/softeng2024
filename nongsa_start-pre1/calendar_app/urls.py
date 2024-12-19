from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),  # /calendar/ 경로에 대한 처리가 필요합니다.
]
