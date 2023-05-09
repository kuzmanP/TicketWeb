from django.contrib import admin
from ticketing.models import Seat,Ticket,Event,EventManager,Transaction
# Register your models here.
admin.site.register(Seat)
admin.site.register(Ticket)
admin.site.register(Event)
admin.site.register(EventManager)
admin.site.register(Transaction)
