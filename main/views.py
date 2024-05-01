from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from main.models import Product, Category, Currency
from main.serializers import Productserializers


class ProductDetailView(ListAPIView):
    queryset = Product.objects.all()
    permission_classes = ()
    serializer_class = Productserializers

    def get_serializer_context(self):
        context = super().get_serializer_context()
        currency_price = Currency.objects.values_list('price', flat=True).first()
        context['currency_price'] = currency_price
        return context


class ProductByCategory(GenericAPIView):
    permission_classes = ()

    def get(self, request, name):
        category_data = Category.objects.filter(name=name).values_list('id', flat=True)
        currency_price = Currency.objects.values_list('price', flat=True).first()

        if category_data:
            products = Product.objects.filter(category_id=category_data[0])
            serializer = Productserializers(products, many=True, context={'currency_price': currency_price})
            return Response({"products": serializer.data})
        else:
            return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

