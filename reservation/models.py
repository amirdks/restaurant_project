from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='تلفن')
    number = models.IntegerField(verbose_name='تعداد')
    date = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='تاریخ')
    time = models.TimeField(null=True, blank=True, verbose_name='ساعت', auto_now=False, auto_now_add=False)
    file = models.FileField(upload_to='files',null=True, blank=True ,verbose_name='فایل ها')

    def __str__(self):
        return self.name


