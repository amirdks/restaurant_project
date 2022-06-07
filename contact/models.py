from django.db import models


# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='نام')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    message = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    response = models.TextField(blank=True, null=True, verbose_name='متن پاسخ تماس با ما')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.full_name

