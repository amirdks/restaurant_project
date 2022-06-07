from django.urls import path
from . import views

urlpatterns = [
    path('', views.GalleyView.as_view(), name='gallery_page')
]
