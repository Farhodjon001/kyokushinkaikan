from django.urls import path
from .views import NewsListAPIView,NewsUpdateDeleteAPIView

urlpatterns=[
    path('news_list/',NewsListAPIView.as_view(),name="news_list"),
    path("news-update-delete-detail/<int:pk>",NewsUpdateDeleteAPIView.as_view(),name='news_update_delete_detail')
]