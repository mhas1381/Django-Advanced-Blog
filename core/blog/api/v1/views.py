from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import PostSerializer,CategorySerializer
from ...models import Post,Category
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination

class PostModelViewSet(viewsets.ModelViewSet):
    ''' getting detail of the post ,edit and removing it'''
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination

class CategoryModelViewSet(viewsets.ModelViewSet):
    ''' getting detail of the categories ,edit and removing it'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()






'''
from rest_framework.decorators import api_view, permission_classes
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
@permission_classes([IsAuthenticated])
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
        '''


"""class PostList(APIView):
    '''getting list of posts and creating post new posts'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        '''retreive a list of posts'''
        if request.method == "GET":
            posts = Post.objects.filter(status=1)
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)

    def post(self, request):
        '''creating a new post with provided data'''
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""





"""class PostDetail(APIView):
    ''' getting detail of the post ,edit and removing it'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        ''' retriving the post data'''
        post = get_object_or_404(Post, pk=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        ''' editing the post data'''
        post = get_object_or_404(Post, pk=id)
        serializer = self.serializer_class(post)
        serializer.is_valid(rasise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        ''' deleting the post object'''
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response({'details': 'post removed succesfully'})"""


# class PostList(ListCreateAPIView):
#     '''getting list of posts and creating post new posts'''
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)

# class PostDetail(RetrieveUpdateDestroyAPIView):
#     ''' getting detail of the post ,edit and removing it'''
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)