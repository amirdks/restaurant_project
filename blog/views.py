from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormMixin
# Create your views here.
from django.views.generic import ListView, DetailView
from online_users.models import OnlineUserActivity

from utils.http_service import get_client_ip
from .forms import BlogCommentForm
from .mixins import BlogMixins
from .models import Blog, BlogTag, BlogCategory, BlogComments, BlogVisit, BlogLike


class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog
    paginate_by = 2
    context_object_name = 'blogs'

    def get_queryset(self):
        query = super(BlogListView, self).get_queryset()
        tag_name = self.kwargs.get('tag')
        category_name = self.kwargs.get('cat')
        if tag_name:
            query = query.filter(tags__slug=tag_name)
            return query
        elif category_name:
            query = query.filter(category__slug=category_name)
            return query
        else:
            return query



# class BlogDetailView(FormMixin, DetailView):
#     model = Blog
#     template_name = 'blog/blog_detail.html'
#     context_object_name = 'blog'
#     form_class = BlogCommentForm
#
#     def get_context_data(self, **kwargs):
#         context = super(BlogDetailView, self).get_context_data(**kwargs)
#         blog: Blog = context.get('object')
#         context['tags'] = BlogTag.objects.all().filter(blogs=blog)
#         context['recents'] = Blog.objects.order_by('-created_at')[:5]
#         context['categories'] = BlogCategory.objects.all()
#         context['comments'] = BlogComments.objects.filter(blog=blog)
#         return context


class BlogDetailView(View):
    def get(self, request: HttpRequest, pk):
        blog = Blog.objects.get(pk=pk)
        tags = BlogTag.objects.all().filter(blogs=blog)
        recents = Blog.objects.order_by('-created_at')[:5]
        categories = BlogCategory.objects.all()
        comments = BlogComments.objects.filter(blog=blog)
        user_ip = get_client_ip(request)
        user_id = None
        if request.user.is_authenticated:
            user_id = request.user.id
        has_been_visited = BlogVisit.objects.filter(ip__iexact=user_ip, blog_id=blog.id).exists()
        if not has_been_visited:
            new_visit = BlogVisit(ip=user_ip, user_id=user_id, blog_id=blog.id)
            new_visit.save()

        blog_visit = blog.blogvisit_set.filter(blog_id=blog.id).count()
        blog_like_count = BlogLike.objects.filter(blog_id=pk).count()
        context = {
            'blog': blog,
            'tags': tags,
            'recents': recents,
            'categories': categories,
            'comments': comments,
            'blog_visit': blog_visit,
            'blog_like_count':blog_like_count,
        }
        return render(request, 'blog/blog_detail.html', context)

    def post(self, request: HttpRequest, pk):
        blog = Blog.objects.get(pk=pk)
        tags = BlogTag.objects.all().filter(blogs=blog)
        recents = Blog.objects.order_by('-created_at')[:5]
        categories = BlogCategory.objects.all()
        comments = BlogComments.objects.filter(blog=blog)

        context = {
            'blog': blog,
            'tags': tags,
            'recents': recents,
            'categories': categories,
            'comments': comments,
        }
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            new_comment = BlogComments(name=name, email=email, text=text, blog=blog)
            new_comment.save()
            return render(request, 'blog/blog_detail.html', context)


def blog_like(request, id):
    blog = Blog.objects.get(pk=id)
    user = request.user
    new_like = BlogLike(user=user, blog=blog)
    new_like.save()
    return redirect(reverse('blog_list_page'))


def aha(request):
    return redirect(reverse('blog_list_page'))
