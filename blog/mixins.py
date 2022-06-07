from django.http import HttpRequest, Http404


class BlogMixins():
    def dispatch(self,request:HttpRequest, *args, **kwargs):
        if request.user.is_superuser:
            return super(BlogMixins, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404('be to nemirese')