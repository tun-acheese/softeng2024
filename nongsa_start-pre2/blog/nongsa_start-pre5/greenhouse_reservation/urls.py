from django.urls import path
from . import views

app_name = 'greenhouse_reservation'

urlpatterns = [
    path('', views.index, name='index'),  # 메인 페이지
    path('reservation_form/', views.reservation_form, name='reservation_form'),
    path('reservation/success/', views.reservation_success, name='reservation_success'),  # 예약 성공
]












