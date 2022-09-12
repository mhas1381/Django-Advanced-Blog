from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import *

# Create your views here.


def indexView(request):
    name = 'ali'
    context = {'name': name}
    return render(request, 'website/index.html', context)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context