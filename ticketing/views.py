from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from ticketing.models import Seat,Ticket,Event
import qrcode
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView

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




import qrcode
from django.http import HttpResponse
from django.template import loader

class UserTicketsView(LoginRequiredMixin, View):
    login_url = 'accounts/signin/'
    redirect_field_name = 'signin'

    def get(self, request):
        # Get all tickets associated with the logged-in user
        tickets = Ticket.objects.filter(user=request.user)

        # Generate QR codes for each ticket
        qr_codes = []
        for ticket in tickets:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(ticket.id)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            qr_codes.append(img)

        context = {
            'tickets': tickets,
            'qr_codes': qr_codes
        }
        return render(request, 'Templates/page.html', context)



class EventListView(LoginRequiredMixin,View):
    login_url = '/signin/'
    redirect_field_name = 'signin'
    

    def get(self,request):
        events=Event.objects.all()
        context={
            'events':events
        }
        return render(request, 'Templates/event.html',context)

