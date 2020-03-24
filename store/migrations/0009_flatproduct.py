# Generated by Django 3.0.1 on 2020-03-24 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200323_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ProductForStore')),
            ],
        ),
    ]
