from django import forms

from blog.models import BlogComments


class BlogCommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    text = forms.CharField()


