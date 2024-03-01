from django.contrib import admin
from .models import Product, Image, Category, Currency, IPAddresses


class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    search_fields = ('User', 'ProductName')


admin.site.register((Category, Currency, IPAddresses))

