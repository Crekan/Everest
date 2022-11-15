from django.contrib import admin
from .models import *


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Trademark)
admin.site.register(Characteristics)
