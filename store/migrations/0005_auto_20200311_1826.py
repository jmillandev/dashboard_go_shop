# Generated by Django 3.0.1 on 2020-03-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200310_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]