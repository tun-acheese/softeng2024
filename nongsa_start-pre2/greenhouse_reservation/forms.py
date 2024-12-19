from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['greenhouse', 'rental_period', 'duration', 'name', 'business_plan']

    def clean(self):
        cleaned_data = super().clean()
        greenhouse = cleaned_data.get('greenhouse')
        rental_period = cleaned_data.get('rental_period')
        duration = cleaned_data.get('duration')

        # 가격 계산 로직
        greenhouse_prices = {
            '온실 1': 500000,
            '온실 2': 500000,
            '온실 3': 500000,
            '온실 4': 600000,
            '온실 5': 600000,
            '온실 6': 600000,
        }

        price_per_month = greenhouse_prices.get(greenhouse)
        total_price = price_per_month * duration

        if rental_period == "년":
            total_price *= 12  # 년 단위로 계산

        cleaned_data['total_price'] = total_price
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # total_price를 모델에 저장
        instance.total_price = self.cleaned_data['total_price']
        if commit:
            instance.save()  # 인스턴스를 DB에 저장
        return instance
