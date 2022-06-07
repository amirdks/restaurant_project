from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Food


# class FoodList(ListView):
#     template_name = ''
#     model = Food
#     paginate_by = 3
#     context_object_name = 'foods'

def food_list(request):
    foods = Food.object.type_lunch()
    context = {
        'foods': foods
    }
    return render(request, 'foods/food_list.html', context)


class FoodDetailView(DetailView):
    template_name = 'foods/food_detail.html'
    model = Food

def kharid(request, id):
    food = Food.object.filter(id=id).first()
    food.quantity = food.quantity - 1
    food.save()
    return redirect(reverse('home_page'))


