from django.urls import path

from shop.views import ProductsView, BrandNameView, ProductNameView, BasketView, ExportBasketInExcel, \
    DeleteProductNameView, DeleteBrandNameView, DeleteProductsView, DeleteBasketView

urlpatterns = [
    path('catalog/', ProductsView.as_view()),
    path('catalog/delete/<int:pk>', DeleteProductsView.as_view()),
    path('products/', ProductNameView.as_view()),
    path('products/delete/<int:pk>', DeleteProductNameView.as_view()),
    path('brands/', BrandNameView.as_view()),
    path('brands/delete/<int:pk>', DeleteBrandNameView.as_view()),
    path('basket/', BasketView.as_view()),
    path('basket/delete/<int:pk>', DeleteBasketView.as_view()),
    path('basket/order/', ExportBasketInExcel.as_view())
]
