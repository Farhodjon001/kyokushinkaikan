from django.contrib import admin

from django.contrib import admin
from .models import CoachModel

# Register your models here.
# class CoachAdmin(admin.ModelAdmin):
#     list_display = ['name','last_name','phone']
#     search_fields = ['photo']

admin.site.register(CoachModel)
