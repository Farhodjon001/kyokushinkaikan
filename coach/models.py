from django.db import models

# Create your models here.

class CoachModel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    rank=models.CharField(max_length=25)
    photo=models.ImageField(upload_to='coachs/',null=True,blank=True)
