from rest_framework import generics
from .serializers import *


class SliderAPIView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
