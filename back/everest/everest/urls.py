from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),
    path('', include('product.urls')),
    path('', include('news.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
