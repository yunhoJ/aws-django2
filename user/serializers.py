from rest_framework import serializers
from user.models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= '__all__'