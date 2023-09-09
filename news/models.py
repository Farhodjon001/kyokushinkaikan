from django.db import models

# Create your models here.
class NewsModel(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    photo=models.ImageField(upload_to='news/', null=True,blank=True)
    created_time=models.DateField(auto_now_add=True)
    updated_time=models.DateField(auto_now=True)