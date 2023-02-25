from rest_framework import serializers
from django.contrib.auth.models import User
from ticketing.models import Seat,Ticket
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model= Seat
        fields=['row','available']   
    
    def create(self, validated_data):
        seat = Seat.objects.create(
            row=validated_data['row'],
            available=validated_data['available'],
           
            
            
        )
        seat.save()
        return seat