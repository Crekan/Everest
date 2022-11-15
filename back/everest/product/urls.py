from django.urls import path, include

from .router import *

urlpatterns = [
    path('product/', include(router.urls)),
]
