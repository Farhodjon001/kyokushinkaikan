from django.urls import path
from .views import GYMListApieview,GYMDetailsApieview,GYMUpdateApieview,GYMDeleteApieview,GYMCreateApieview
urlpatterns=[
    path('gym_all/',GYMListApieview.as_view()),
    path('create/<int:pk>/',GYMCreateApieview.as_view()),
    path('delete/<int:pk>/',GYMDeleteApieview.as_view()),
    path('update/<int:pk>/',GYMUpdateApieview.as_view()),
    path('details/<int:pk>/',GYMDetailsApieview.as_view())
]