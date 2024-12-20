from django import forms

class ReservationForm(forms.Form):
    GREENHOUSE_CHOICES = [
        ('온실 1', '온실 1 (50평)'),
        ('온실 2', '온실 2 (50평)'),
        ('온실 3', '온실 3 (50평)'),
        ('온실 4', '온실 4 (50평)'),
        ('온실 5', '온실 5 (50평)'),
        ('온실 6', '온실 6 (50평)'),
    ]

    RENTAL_PERIOD_CHOICES = [
        ('개월', '개월'),
        ('년', '년'),
    ]

    greenhouse = forms.ChoiceField(choices=GREENHOUSE_CHOICES, required=True, label='온실 선택')
    rental_period = forms.ChoiceField(choices=RENTAL_PERIOD_CHOICES, required=True, label='대여 기간')
    duration = forms.IntegerField(min_value=1, required=True, label='대여 기간 (숫자)')
    name = forms.CharField(max_length=100, required=True, label='성함')
    business_plan = forms.FileField(required=True, label='사업계획서 제출')
    
    # 가격을 계산하기 위한 메소드 추가
    def calculate_price(self):
        prices = {
            "온실 1": 500000,
            "온실 2": 500000,
            "온실 3": 500000,
            "온실 4": 600000,
            "온실 5": 600000,
            "온실 6": 600000,
        }

        greenhouse = self.cleaned_data.get('greenhouse')
        rental_period = self.cleaned_data.get('rental_period')
        duration = self.cleaned_data.get('duration')

        price_per_month = prices.get(greenhouse, 0)
        total_price = price_per_month * duration

        if rental_period == "년":
            total_price *= 12

        return total_price
