from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('news_title',)}


admin.site.register(Slider)
admin.site.register(Ip)
admin.site.register(News, NewsAdmin)
