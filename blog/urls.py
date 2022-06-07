from django.urls import path
from . import views
urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list_page'),
    path('<pk>', views.BlogDetailView.as_view(), name='blog_detail_page'),
    path('tag/<slug:tag>', views.BlogListView.as_view(), name='blog_tag'),
    path('cat/<slug:cat>', views.BlogListView.as_view(), name='blog_category'),
    path('like/<id>', views.blog_like, name='blog_like'),
]