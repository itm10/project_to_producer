from django.contrib import admin
from .models import Product, Image, Category, Currency


class ProductImageInline(admin.TabularInline):
    model = Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    search_fields = ('name', 'description')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ('image',)


admin.site.register((Category, Currency))
