from django.db import models

from users.models import UserAccount


class ProductName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BrandName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.ForeignKey(ProductName, on_delete=models.PROTECT, blank=True, null=True)
    brand_name = models.ForeignKey(BrandName, on_delete=models.PROTECT, blank=True, null=True)
    article = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', blank=True, null=True)


class Basket(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

