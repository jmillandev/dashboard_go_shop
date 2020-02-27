# Generated by Django 3.0.1 on 2020-02-27 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0031_auto_20200212_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination_place',
            field=models.CharField(default='Venezuela', max_length=255),
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raiting', models.IntegerField(choices=[(-1, 'Negativo.'), (0, 'Neutral.'), (1, 'Positivo.')])),
                ('reason', models.IntegerField(choices=[(0, 'Me quede sin stock.'), (1, 'No pude contactar al comprador.'), (2, 'El Comprador no tenia suficiente dinero.'), (3, 'El comprador decidio no comprar.')], null=True)),
                ('fulfilled', models.BooleanField()),
                ('message', models.CharField(max_length=159)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.localtime)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
