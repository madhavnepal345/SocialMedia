from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post,Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','passeord']
        extra_kwargs={'password':{'write_only':True}}


