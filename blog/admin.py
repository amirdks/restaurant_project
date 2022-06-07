from django.contrib import admin
from django.contrib.auth.models import User


class BlogAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['queryset'] = User.objects.filter(is_staff=True)
            return super(BlogAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)



class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
from blog.models import Blog, BlogCategory, BlogTag, BlogComments, BlogVisit, BlogLike

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogTag)
admin.site.register(BlogComments)
admin.site.register(BlogVisit)
admin.site.register(BlogLike)
