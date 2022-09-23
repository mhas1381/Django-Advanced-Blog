from django.urls import path
from blog import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


app_name = 'blog'
urlpatterns = [
    # path('fbv-index', views.indexView, name='fbv-index'),
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('post/', views.PostList.as_view(), name='post-list'),
    path('go-to-maktabkhooneh',
         views.RedirectToMaktab.as_view(), name='go-to-maktabkhoone')
]
