from django.contrib import admin

from shop.models import ProductName, BrandName, Product, Basket

admin.site.register(ProductName)
admin.site.register(BrandName)
admin.site.register(Product)
admin.site.register(Basket)
