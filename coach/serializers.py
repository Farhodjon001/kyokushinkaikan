from .models import CoachModel
from rest_framework import serializers
class CouchSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoachModel
        fields = ('first_name','last_name','rank','photo','date_of_birth')