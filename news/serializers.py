from .models import NewsModel
from rest_framework import serializers

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        modulel=NewsModel
        fields='__all__'