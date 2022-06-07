# Generated by Django 4.0.3 on 2022-04-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_food_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('B', 'صبحانه'), ('D', 'نوشیدنی'), ('DI', 'شام'), ('L', 'نهار')], default='D', max_length=10, verbose_name='نوع غذا'),
        ),
    ]
