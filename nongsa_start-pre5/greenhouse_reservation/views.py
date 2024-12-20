from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReservationForm
from .models import Reservation  # Reservation 모델이 있다고 가정

# 메인 페이지 렌더링
def index(request):
    return render(request, 'index.html')  # index.html 템플릿 반환

# 예약 폼 페이지
def reservation_form(request):
    if request.method == "POST":
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            # 폼 데이터를 클린(cleaned_data)으로 가져옴
            total_price = form.calculate_price()
            name = form.cleaned_data['name']
            greenhouse = form.cleaned_data['greenhouse']
            duration = form.cleaned_data['duration']
            rental_period = form.cleaned_data['rental_period']

            # DB에 저장 (Reservation 모델 사용)
            reservation = Reservation(
                name=name,
                greenhouse=greenhouse,
                duration=duration,
                rental_period=rental_period,
                total_price=total_price,  # 필요한 경우 모델에 필드 추가
            )
            reservation.save()

            # 예약 성공 페이지로 리다이렉트 (id를 pk로 전달)
            return redirect('reservation_success', pk=reservation.pk)

    else:
        form = ReservationForm()

    return render(request, 'reservation_form.html', {'form': form})

# 예약 성공 페이지
def reservation_success(request, pk):
    try:
        # 예약 정보 가져오기
        reservation = Reservation.objects.get(pk=pk)
        context = {
            'name': reservation.name,
            'greenhouse': reservation.greenhouse,
            'duration': reservation.duration,
            'rental_period': reservation.rental_period,
            'total_price': reservation.total_price,
        }
        return render(request, 'reservation_success.html', context)
    
    except Reservation.DoesNotExist:
        # 예약이 존재하지 않으면 404 오류 처리
        return HttpResponse("예약 정보를 찾을 수 없습니다.", status=404)
