from django.urls import path
<<<<<<< HEAD

from main.views import ProductDetailView, ProductByCategory

urlpatterns = [
    path('products-get', ProductDetailView.as_view()),
    path('products-bycategory/<str:name>', ProductByCategory.as_view()),
=======
from .views import ProductDetailView, ProductByCategory

urlpatterns = [
    path('get-products', ProductDetailView.as_view(), name='get_products'),
    path('product-bycategory/<str:name>', ProductByCategory.as_view(), name='products_bycategory'),
>>>>>>> 1d9f52e (Ready)
]
