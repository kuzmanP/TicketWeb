from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class EventManager(models.Model):
    manager_id = models.UUIDField(primary_key=True,  default=uuid.uuid4, editable=False)
    manager_name=models.CharField(max_length=1000)
    manager_contact=models.CharField(max_length=10)
    def __str__(self):
            return f"{self.manager_id} - {self.manager_name}"

    def __unicode__(self):
        return 
    
class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event_name=models.CharField(max_length= 1000)
    event_location = models.CharField(max_length= 1000)
    event_attendees_number = models.IntegerField()
    event_manager=models.ForeignKey(EventManager, on_delete=models.CASCADE)
    time_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.event_id} - {self.event_name} - {self.time_created}"

    def __unicode__(self):
        return 
#Seat Model
class Seat(models.Model):
    row = models.CharField(max_length=100000)
    number = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.row} - {self.number}"
    
    
PaymentTypeCHOICES = [
    ("C", "Cash"),
    ("M", "MOMO"),
    ("CQ", "CHEQUE")
]
class Transaction(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type=models.CharField(choices=PaymentTypeCHOICES,max_length=100,default="Regular", )
    amount = models.IntegerField()
    transaction_date=models.DateField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 



TicketTypeCHOICES = [
    ("Rg", "Regular"),
    ("V", "VIP"),
    ("VV", "VVIP")
]
class Ticket(models.Model):
    ticket_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket_type=models.CharField(choices=TicketTypeCHOICES,max_length=1000, default="Regular")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    event_name=models.CharField(max_length=1000, default="Piloting Event")
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.seat} - {self.ticket_type} - {self.event_name}"    



