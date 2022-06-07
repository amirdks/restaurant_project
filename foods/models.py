from django.db import models

# Create your models here.
from django.utils.html import format_html


class FoodManager(models.Manager):
    def type_lunch(self):
        return self.filter(type_food='lunch')


class Food(models.Model):
    FOOD_TYPE = [
        ("breakfast", "صبحانه"),
        ("drinks", "نوشیدنی"),
        ("dinner", "شام"),
        ("lunch", "نهار"),
    ]
    name = models.CharField(max_length=100, verbose_name='اسم غدا')
    description = models.CharField(max_length=50, verbose_name='توضیحات عذا')
    rate = models.IntegerField(default=0, verbose_name='امتیاز')
    price = models.IntegerField(verbose_name='قیمت')
    quantity = models.PositiveIntegerField(default=1, verbose_name='موجودی')
    time = models.IntegerField(verbose_name='مدت زمان')
    pub_date = models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار', auto_now=False)
    photo = models.ImageField(upload_to='images/foods', verbose_name='تصویر عذا')
    slug = models.SlugField(default='', null=False, db_index=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    type_food = models.CharField(verbose_name='نوع غذا', max_length=10, choices=FOOD_TYPE, default="drinks")

    def __str__(self):
        return self.name

    def photo_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.photo.url))

    photo_tag.short_description = 'عکس'

    object = FoodManager()
