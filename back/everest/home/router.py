from rest_framework import routers

from .api import *

router = routers.DefaultRouter()
router.register('slider/api', SliderViewSet, 'slider')
router.register('category/api', CategoryViewSet, 'category')
