# Generated by Django 3.0.1 on 2020-01-29 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_attribute_value_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='value_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
