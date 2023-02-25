from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from ticketing.models import Seat,Ticket
# Create your views here.

def purchase_ticket(request, seat_id):
    seat = Seat.objects.get(pk=seat_id)
    if not seat.available:
        # Seat has already been purchased
        return redirect('seat_chart')
    ticket = Ticket.objects.create(user=request.user, seat=seat)
    seat.available = False
    seat.save()
    return redirect('ticket_detail', ticket_id=ticket.id)