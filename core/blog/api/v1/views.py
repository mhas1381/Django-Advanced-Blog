from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from rest_framework import status

from ...models import Post


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=1)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT" , "DELETE"])
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post , data = request.data)
        serializer.is_valid(raise_exception)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({'details':'post removed succesfully'})