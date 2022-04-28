from django.contrib import admin

from shop.models import Category, Shop, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'shop', 'image']
    list_filter = ['name']
    search_fields = ['name', 'category']
    fields = ['name', 'category', 'shop', 'image']


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)

