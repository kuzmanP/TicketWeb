from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields=['bio','contact','User_type','user']   
    
    def create(self, validated_data):
        profile = Profile.objects.create(
            bio=validated_data['bio'],
            contact=validated_data['contact'],
            User_type=validated_data['User_type'],
            user=validated_data['user']
            
            
        )
        profile.save()
        return profile