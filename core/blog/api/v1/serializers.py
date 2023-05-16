from rest_framework import serializers
from blog.models import Post,Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 255)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id' , 'name']

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source = 'get_snippet')
    relative_url = serializers.URLField(source= 'get_absolute_api_url' , read_only=True)
    absolute_url = serializers.SerializerMethodField()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'title', 'content', 'snippet','category','relative_url','absolute_url','status', 'published_date', ]

    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

