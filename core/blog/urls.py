from django.urls import path
from blog import views
from django.views.generic import TemplateView

urlpatterns = [
    path('fbv-index', views.indexView, name='fbv-index')
]
