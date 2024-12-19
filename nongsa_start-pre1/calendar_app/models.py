from django.db import models

class Event(models.Model):
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.date}: {self.description}"
