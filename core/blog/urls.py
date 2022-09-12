from django.urls import path
from blog import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


app_name = 'blog'
urlpatterns = [
    path('fbv-index', views.indexView, name='fbv-index'),
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('go-to-index',
         RedirectView.as_view(pattern_name="blog:cbv-index"), name='go-to-index')
]
