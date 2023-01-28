from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ...models import Post


@api_view()
def post_list(request):
    posts = Post.objects.filter(status=1)
    serializer = PostSerializer(posts , many = True)
    return Response(serializer.data)


@api_view()
def post_detail(request, id):

    post = get_object_or_404(Post , pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)
