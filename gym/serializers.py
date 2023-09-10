from rest_framework import serializers
from .models import GymModel
class GymSerializers(serializers.ModelSerializer):
    class Meta:
         model = GymModel
         fields = '__all__'