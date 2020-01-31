from django.db import models
from store.models import Seller
from django.utils import timezone

class Category(models.Model):
    id = models.PositiveIntegerField(
        help_text="Identificador unico de la categoria en mercadolibre sin el prefijo MLV",
        primary_key=True
    )
    father = models.PositiveIntegerField()
    approved = models.BooleanField(default=False)
    name = models.CharField(max_length=60)

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    cost_price = models.FloatField(null=True)
    sale_price = models.FloatField(null=True)
    provider_sku = models.CharField(max_length=50, unique=True)
    provider_link = models.CharField(max_length=255, unique=True)
    sku = models.CharField(max_length=20, unique=True, null=True, default=None)
    image = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, default=None)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField()
    last_update = models.DateTimeField(default=timezone.localtime)
    modifiable = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Picture(models.Model):
    src =  models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Attribute(models.Model):
    id_meli = models.CharField(max_length=50)
    value = models.CharField(max_length=200)
    value_id = models.CharField(max_length=50, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_meli