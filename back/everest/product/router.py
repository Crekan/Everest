from .api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', ProductViewSet)
