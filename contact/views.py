from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from contact.forms import ContactUsForm
from contact.models import ContactUs


class ContactUsView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contact/contact_us_page.html'
    success_url = reverse_lazy('home_page')


