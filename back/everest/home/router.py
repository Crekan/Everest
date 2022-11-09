from .api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('slider', SliderViewSet, 'slider')
router.register('category', CategoryViewSet, 'category')
router.register('news', NewsViewSet, 'news')

