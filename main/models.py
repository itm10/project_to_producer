from os.path import splitext
from django.db import models

from django.template.defaultfilters import slugify


def slugify_upload(instance, filename):
    folder = instance._meta.model_name
    name, ext = splitext(filename)
    name_t = slugify(name) or name
    return f"{folder}/{name_t}{ext}"


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    color = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=slugify_upload)

    def __str__(self):
        return f'{self.product.name} - {self.image.name}'


class Currency(models.Model):
    price = models.FloatField(verbose_name='Currency')

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currency'


class IPAddresses(models.Model):
    ip = models.CharField(max_length=12)

    class Meta:
        verbose_name_plural = 'IPAddresses'







