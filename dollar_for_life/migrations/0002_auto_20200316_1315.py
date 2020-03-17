# Generated by Django 3.0.1 on 2020-03-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dollar_for_life', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='rate',
            new_name='ve',
        ),
        migrations.AddField(
            model_name='history',
            name='do',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='mx',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]