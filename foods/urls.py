from django.urls import path
from . import views
urlpatterns = [
    path('', views.food_list, name='food_list_page'),
    path('<slug:slug>', views.FoodDetailView.as_view(), name='food_detail_page'),
    path('kharid/<int:id>',views.kharid , name='kharid'),
]