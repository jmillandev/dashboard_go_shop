# Generated by Django 3.0.1 on 2020-01-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_product_last_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='destination_place',
            field=models.CharField(default='Venezuela', max_length=255),
        ),
    ]