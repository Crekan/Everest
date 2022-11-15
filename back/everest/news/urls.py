from django.urls import path, include

from .router import router
from .views import *

urlpatterns = [
    path('news/', include(router.urls), name='news'),

    path('posts/<str:slug>/', post_view, name='post'),
]
