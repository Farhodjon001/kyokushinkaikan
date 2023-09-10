from django.urls import path
from views import *
urlpatterns = [
    path('get_all/',ListCoachView.as_view(),name='get_all'),
    path('get_id/<int:pk>/',DetailCoachView.as_view(),name='detail'),
    path('create/',CreateCoachView.as_view(),name='create'),
    path('delete/<int:pk>/',DeleteCoachView.as_view(),name='delete'),
]