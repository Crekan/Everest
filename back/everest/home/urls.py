from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/sliderlist/', SliderAPIView.as_view()),
]