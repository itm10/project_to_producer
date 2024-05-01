from django.urls import path
from main.views import ProductDetailView, ProductByCategory

urlpatterns = [
    path('products-get', ProductDetailView.as_view()),
    path('products-bycategory/<str:name>', ProductByCategory.as_view()),
]
