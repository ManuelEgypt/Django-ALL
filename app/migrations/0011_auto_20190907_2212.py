# Generated by Django 2.1.5 on 2019-09-07 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190907_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
