# Generated by Django 4.0.2 on 2022-04-13 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogtag_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='blogs', to='blog.BlogTag', verbose_name='تگ ها'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام کاربری')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('text', models.TextField(verbose_name='متن نظر')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog', verbose_name='مقاله')),
            ],
        ),
    ]
