from django.urls import path,include
from . import views


app_name = 'api-v1'

urlpatterns = [
    path('post/',views.post_list,name='post-list'),

]