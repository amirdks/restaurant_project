from django.db import models

# Create your models here.
from django.utils.html import format_html


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/gallery', verbose_name='عکس')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_read = models.BooleanField()

    def __str__(self):
        return self.title

    def mini_image(self):
        return format_html("<img width=100 jeight=75 style='border-radius=5px;' src='{}'>".format(self.image.url))

    mini_image.short_description = 'عکس'

    class Meta:
        verbose_name = 'عکس های گالری'
        verbose_name_plural = 'عکس گالری'
