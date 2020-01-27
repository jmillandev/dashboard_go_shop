# Generated by Django 3.0.1 on 2020-01-21 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200120_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='provider_link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default=None, max_length=20, null=True, unique=True),
        ),
    ]
