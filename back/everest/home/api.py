from rest_framework import viewsets, permissions

from .serializers import *


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SliderSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer
