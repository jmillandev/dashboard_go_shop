# Generated by Django 3.0.1 on 2020-03-18 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200316_2119'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ProductForStore'),
        ),
    ]
