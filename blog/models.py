from django.contrib.auth.models import User
from django.db import models
from django.http import HttpRequest
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.CharField(max_length=100, verbose_name='توضیحات')
    content = RichTextUploadingField()
    created_at = models.DateTimeField(verbose_name='زمان انتشار', default=timezone.now)
    author = models.ForeignKey(to=User, verbose_name='نویسنده', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/blog', blank=True, null=True, verbose_name='تصویر')
    category = models.ForeignKey(related_name='blog', blank=True, null=True, to='BlogCategory',
                                 on_delete=models.CASCADE, verbose_name='دسته بندی')
    tags = models.ManyToManyField(blank=True, to='BlogTag', verbose_name='تگ ها', related_name='blogs')

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=50)
    slug = models.SlugField(verbose_name='عنوان در url')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')

    def __str__(self):
        return self.title


class BlogTag(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=50)
    slug = models.SlugField(verbose_name='عنوان در url')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')
    update_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت')

    def __str__(self):
        return self.title


class BlogComments(models.Model):
    blog = models.ForeignKey(to='Blog', verbose_name="مقاله", related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='نام کاربری')
    email = models.EmailField(verbose_name='ایمیل', max_length=254)
    text = models.TextField(verbose_name='متن نظر')
    date = models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')

    def __str__(self):
        return self.email


class BlogVisit(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, verbose_name="مقاله")
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='کاربر')


class BlogLike(models.Model):
    blog = models.ForeignKey('Blog', related_name='blog_like',on_delete=models.CASCADE, verbose_name='بلاگ')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_like', verbose_name='کاربر')

    def __str__(self):
        return self.blog.title


