from .models import CoachModel
from rest_framework import serializers
class CouchSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoachModel
        fields = ('name','last_name','phone','image')