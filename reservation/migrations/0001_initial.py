# Generated by Django 4.0.2 on 2022-04-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=200, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=20, verbose_name='تلفن')),
                ('number', models.IntegerField(verbose_name='تعداد')),
                ('date', models.DateField(blank=True, null=True, verbose_name='تاریخ')),
                ('time', models.TimeField(verbose_name='ساعت')),
            ],
        ),
    ]