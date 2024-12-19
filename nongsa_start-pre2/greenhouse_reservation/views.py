# views.py
from django.shortcuts import render, redirect
from .forms import ReservationForm

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')  # 예약 성공 후 리디렉션
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})

def reservation_success(request):
    return render(request, 'reservation_success.html')

