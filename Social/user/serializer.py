from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post,Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','passeord']
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    

class  PostSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    likes_count=serializers.SerializerMethodField()

    class Meta:
        model=Post
        fields=['id','author','content','likes_count','created_at']

    def get_likes_count(self,obj):
        return obj.likes_count()


class CommentSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')


    class Meta:
        model=Comment
        fields=['id','post','author','content','created_at']
