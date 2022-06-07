from django.contrib import admin

# Register your models here.
from gallery.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'mini_image']
    list_editable = ['is_active']


admin.site.register(Gallery, GalleryAdmin)
