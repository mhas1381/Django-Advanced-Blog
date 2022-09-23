from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView,RedirectView
from blog.models import *

# Create your views here.

# function base view to show a template
'''
def indexView(request):
    name = 'ali'
    context = {'name': name}
    return render(request, 'website/index.html', context)
'''
class IndexView(TemplateView):
    '''
    a class based view to show index page
    '''
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context

# FBV for redirect
def redirectToMaktab(request):
    return redirect('https://maktabkhooneh.org')

# CBV for redirect
class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.org'