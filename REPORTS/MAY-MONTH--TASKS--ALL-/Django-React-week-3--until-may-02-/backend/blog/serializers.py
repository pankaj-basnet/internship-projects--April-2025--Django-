from rest_framework import serializers
from .models import Post, Comment, Tag, Like
from api.models import User 
from api.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    author = UserSerializer(read_only=True)  # Use the UserSerializer
    tags = TagSerializer(many=True, read_only=True)
    cover_image = serializers.ImageField(required=False)
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'updated_at', 'created_at', 'status', 'cover_image', 'tags', 'likes_count', 'is_draft' , 'like_count']
        read_only_fields = ['id', 'author', 'updated_at', 'created_at', 'likes', 'slug']

    def get_like_count(self, instance):
        return Like.objects.filter(post=instance).count()
    

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Use the UserSerializer
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'sentences', 'created_at']
        read_only_fields = ['id', 'user', 'post', 'created_at']
        #Change field name from content to sentences to match model.


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']
        read_only_fields = ['id']

    def create(self, validated_data):
        # Prevent duplicate likes for the same user and post
        like, created = Like.objects.get_or_create(
            user=validated_data['user'],
            post=validated_data['post']
        )
        return like