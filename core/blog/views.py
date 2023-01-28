from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView



from blog.models import *
from .forms import PostForm

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

    def get_context_data(self, **kwargs):
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


class PostList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'blog.view_post'
    model = Post
    # queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


'''
class PostCreateView(FormView):
    template_name = 'create-post.html'
    form_class = PostForm
    success_url = '/blog/post'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
'''


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content',
              'status', 'category', 'published_date']
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post'

