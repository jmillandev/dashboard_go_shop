# Generated by Django 3.0.1 on 2020-01-28 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20200128_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='src',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]