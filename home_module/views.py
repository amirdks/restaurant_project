from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

from gallery.models import Gallery

class HomeView(TemplateView):
    template_name = 'home_module/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.all()
        return context


def logout_view(request):
    if  request.user.is_authenticated:
        logout(request)
        return redirect(reverse('home_page'))
    else:
        return redirect(reverse('home_page'))

def site_header_component(request):
    context = {}
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    context = {}
    return render(request, 'shared/site_footer_component.html', context)
