from django.urls import path

from api.views import ProductView

urlpatterns = [
    path('', ProductView.as_view(), name="products_list_view"),
    path('<int:shop_pk>/', ProductView.as_view(), name="shop_products_view"),
    path('<int:shop_pk>/categories/<int:categories_pk>/', ProductView.as_view(), name="shop_categories_products_view"),
    path('<int:shop_pk>/categories/<int:categories_pk>/<int:product_pk>/', ProductView.as_view(), name="product_view")
]
