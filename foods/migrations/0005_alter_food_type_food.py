# Generated by Django 4.0.3 on 2022-04-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_food_type_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('breakfast', 'صبحانه'), ('drinks', 'نوشیدنی'), ('dinner', 'شام'), ('lunch', 'نهار')], default='drinks', max_length=10, verbose_name='نوع غذا'),
        ),
    ]
