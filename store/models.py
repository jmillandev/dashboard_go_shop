from django.db import models


class Seller(models.Model):
    nickname = models.CharField(max_length=60, unique=True, null=True)
    id = models.PositiveIntegerField(
        help_text="Identificador unico del vendedor en la WEB/API del proveeedor",
        primary_key=True
    )
    bad_seller = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}:{self.nickname}'

class BusinessModel(models.Model):
    """
    Aqui esta todas las variables que se le aplicaran a cada precio de costo por producto
    """
    seller_id = models.PositiveIntegerField(
        primary_key=True,
        help_text="Identificador unico del vendedor en la API de mercadolibre",
    )
    trm = models.FloatField(
        help_text="Conversion de la moneda del proveedor a 1 USD.",
    )
    shipping = models.FloatField(
        help_text="Costo MAXIMO de envio dentro del pais es decir la ultima milla(en USD).",
    )
    meli_tax = models.FloatField(
        help_text="PORCENTAJE de la comision de mercadolibre.",
    )
    utility = models.IntegerField(
        help_text="PORCENTAJE de la utilidad de los socios.",
    )
    usd_variation = models.FloatField(
        help_text="Precio de actualizacion del USD por encima de la taza.",
        default=0
    )
    name = models.CharField(
        max_length=10,
        help_text="Nombre de la tienda. Max 10 caracteres")
    
    country = models.CharField(
        max_length=2,
        help_text="Abreviatura del pais online. Ej: ve, co, do, mx"
    )

class Buyer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nickname= models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.PositiveIntegerField(default=None, null=True)
    email = models.EmailField(max_length=70, null=True)

    def __str__(self):
        return f'{self.id}:{self.nickname}'

class BadWord(models.Model):
    word = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.word