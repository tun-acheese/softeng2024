# models.py
from django.db import models

class Reservation(models.Model):
    GREENHOUSE_CHOICES = [
        ('온실 1', '온실 1 (50평)'),
        ('온실 2', '온실 2 (50평)'),
        ('온실 3', '온실 3 (50평)'),
        ('온실 4', '온실 4 (50평)'),
        ('온실 5', '온실 5 (50평)'),
        ('온실 6', '온실 6 (50평)'),
    ]
    rental_period_choices = [
        ('개월', '개월'),
        ('년', '년'),
    ]

    greenhouse = models.CharField(max_length=10, choices=GREENHOUSE_CHOICES)
    rental_period = models.CharField(max_length=5, choices=rental_period_choices)
    duration = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    business_plan = models.FileField(upload_to='business_plans/')
    total_price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} 예약 ({self.greenhouse}, {self.duration} {self.rental_period})"
