from django.db import models

# Create your models here.

#Seat Model
class Seat(models.Model):
    row = models.CharField(max_length=10)
    number = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.row} - {self.number}"