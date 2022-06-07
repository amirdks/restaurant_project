# Generated by Django 4.0.3 on 2022-04-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_food_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True, verbose_name='عنوان در url'),
        ),
    ]
