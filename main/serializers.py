from rest_framework import serializers

from main.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class Productserializers(serializers.ModelSerializer):
    category = CategorySerializer()
    images = serializers.SerializerMethodField()
    price_after_currency = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'color', 'images', 'category', 'price_after_currency')

    def get_images(self, obj):
        images = obj.image_set.all()
        print(images)
        image_url = [image.image.url for image in images]
        print(image_url)
        return image_url

    def get_price_after_currency(self, obj):
        currency_price = self.context.get('currency_price', 1)
        if currency_price is None:
            return "Currency price not specified"
        return obj.price * currency_price

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        currency_price = self.context.get('currency_price', 1)

        representation['dollar'] = currency_price
        return representation
