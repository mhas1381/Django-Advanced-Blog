from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import *

# Create your views here.


def indexView(request):
    name = 'ali'
    context = {'name': name}
    return render(request, 'website/index.html', context)
