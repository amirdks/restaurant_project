from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView

from reservation.forms import ReservationForm
from reservation.models import Reservation


class ReservationView(CreateView):
    template_name = 'reservation/reservation_form.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('home_page')




