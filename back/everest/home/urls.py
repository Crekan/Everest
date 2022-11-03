from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/sliderlist/', SliderAPIView.as_view()),
    path('api/v1/news/', NewsAPIView.as_view()),

    path('posts/<str:slug>/', post_view, name='post'),
]
