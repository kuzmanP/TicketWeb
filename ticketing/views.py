from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
=======
from django.shortcuts import render,redirect
from ticketing.models import Seat,Ticket
import qrcode
from django.http import HttpResponse
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



def generate_qr_code(request, ticket_id):
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(ticket_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    
    # Return the image as an HTTP response
    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response
>>>>>>> origin/main
