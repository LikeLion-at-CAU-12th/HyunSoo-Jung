from rest_framework import serializers
from .models import *

import boto3
from django.conf import settings
from uuid import uuid4


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"