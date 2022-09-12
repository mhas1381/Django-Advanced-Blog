from django.urls import path
from blog import views
from django.views.generic import TemplateView

urlpatterns = [
    path('fbv-index', views.indexView, name='fbv-index'),
    path('cbv-index',views.IndexView.as_view() , name='cbv-index')
]
