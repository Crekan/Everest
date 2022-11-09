from django.urls import path, include

from .views import *
from .router import *

urlpatterns = [
    path('product/', include(router.urls)),
]
