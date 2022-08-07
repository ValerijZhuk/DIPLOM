from django.urls import path

from shop.views import ProductsView, BrandNameView, ProductNameView, BasketView, ExportBasketInExcel

urlpatterns = [
    path('catalog/', ProductsView.as_view()),
    path('products/', ProductNameView.as_view()),
    path('brands/', BrandNameView.as_view()),
    path('basket/', BasketView.as_view()),
    path('basket/order/', ExportBasketInExcel.as_view())
]