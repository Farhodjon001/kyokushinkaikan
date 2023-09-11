from django.db import models
from coach.models import CoachModel
# Create your models here.
class GymModel(models.Model):
    name=models.CharField(max_length=50)
    coach=models.ForeignKey(CoachModel,on_delete=models.CASCADE)
    location=models.URLField(null=True,blank=True,default='')
    phote=models.ImageField(upload_to='gyms/',null=True,blank=True)
    phone=models.CharField(max_length=13)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'GYM'
