from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название категории")

    def __str__(self):
        return f"{self.name}"


class Shop(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название магазина")

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Категория', related_name="product_category")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Магазин", related_name="product_shop")
    image = models.ImageField(null=True, blank=True, upload_to='product_pic', verbose_name='Картинка')
    update_counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
