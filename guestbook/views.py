from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

# Swagger
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
# from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# GenericAPIView
from rest_framework import generics

from guestbook.models import *
from .serializers import *
import json
import datetime

# Create your views here.

# 방명록 작성 기능 (POST)
# 제목, 작성자, 내용, 게시글 비밀번호 입력받기
class GuestBookPost(generics.CreateAPIView):
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer


# 방명록 조회 기능 (GET)
class GuestBookGet(generics.RetrieveAPIView):
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer
    lookup_feild = 'pk'


# 방명록 삭제 기능 (DELETE)
# 올바른 게시글 비밀번호를 입력하면 삭제 가능
class GuestBookDelete(generics.DestroyAPIView):
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer
    lookup_field = 'pk'


# 방명록 리스트 기능
# 방명록 보여주기
class GuestBookList(generics.ListAPIView):
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer

# 방명록 시간 순 정렬
# class GuestBookListSort(generics.RetrieveAPIView):
#     queryset = GuestBook.objects.order_by('-created_at')
#     serializer_class = GuestBookSerializer

class GuestBookListSort(generics.ListAPIView):
    serializer_class = GuestBookSerializer

    def get_queryset(self):
        return GuestBook.objects.order_by('-created_at')