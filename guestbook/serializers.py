from rest_framework import serializers
from .models import *

class GuestBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestBook
        fields = "__all__"