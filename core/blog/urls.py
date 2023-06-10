from django.urls import path, include
from blog import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


app_name = "blog"
urlpatterns = [
    # path('fbv-index', views.indexView, name='fbv-index'),
    path("cbv-index", views.IndexView.as_view(), name="cbv-index"),
    path("post/", views.PostList.as_view(), name="post-list"),
    # path('go-to-maktabkhooneh',
    #      views.RedirectToMaktab.as_view(), name='go-to-maktabkhoone')
    path(
        "post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"
    ),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path(
        "post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"
    ),
    path(
        "post/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
