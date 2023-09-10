from django.shortcuts import render
from .serializers import CouchSerializers
from rest_framework import generics
from .models import CoachModel
# Create your views here.
class DetailCoachView(generics.RetrieveAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CouchSerializers

# class DetailCoachView(APIView):
#     def get(self,request,*args,**kwargs):
#         Coach = get_object_or_404(CoachModel, id=kwargs['id'])
#         serializer = TrainersSerializers(Coach)
#         return Response(serializer.data)
class CreateCoachView(generics.CreateAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CouchSerializers
class ListCoachView(generics.ListAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CouchSerializers

class DeleteCoachView(generics.DestroyAPIView):
    queryset = CoachModel.objects.all()
    serializer_class = CouchSerializers
