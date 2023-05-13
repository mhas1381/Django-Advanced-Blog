from rest_framework import serializers
from blog.models import Post,Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 255)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'title', 'content', 'status', 'published_date', ]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id' , 'name']