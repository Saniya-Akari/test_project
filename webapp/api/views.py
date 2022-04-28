from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProductSerializer
from shop.models import Product


class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        if kwargs.get('product_pk'):
            objects = get_list_or_404(Product, shop_id=kwargs['shop_pk'], category_id=kwargs['categories_pk'], pk=kwargs['product_pk'])
        elif len(kwargs) == 0:
            objects = Product.objects.all()
        elif kwargs.get('categories_pk'):
            objects = get_list_or_404(Product, shop_id=kwargs['shop_pk'], category_id=kwargs['categories_pk'])
            paginator = Paginator(objects, 5)
            page = request.GET.get('page')
            if page:
                try:
                    objects = paginator.page(page)
                except PageNotAnInteger:
                    objects = paginator.page(1)
                except EmptyPage:
                    return Response("Такой страницы нет")
        else:
            objects = get_list_or_404(Product, shop_id=kwargs['shop_pk'])
        serializer = ProductSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        objects = get_object_or_404(Product, shop_id=kwargs['shop_pk'], category_id=kwargs['categories_pk'], pk=kwargs['product_pk'])
        serializer = ProductSerializer(objects, request.data)
        if serializer.is_valid():
            product = serializer.save()
            objects.update_counter += 1
            objects.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
