from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

#Seat Model
class Seat(models.Model):
    row = models.CharField(max_length=100000)
    number = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.row} - {self.number}"
    
class Ticket(models.Model):
    ticket_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.seat}"    