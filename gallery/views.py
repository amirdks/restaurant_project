from django.shortcuts import render

# Create your views here.
from django.views import View

from gallery.models import Gallery


class GalleyView(View):
    def get(self, request):
        context = {
            'images': Gallery.objects.filter(is_active=True)
        }
        return render(request, 'gallery/gallery.html', context)
