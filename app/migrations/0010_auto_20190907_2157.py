# Generated by Django 2.1.5 on 2019-09-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190907_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
