from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from posts.models import *
import json
import datetime

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'index.html')

# 3주차
# def hello_world(request):
#     if request.method == "GET":
#         return JsonResponse({
#             'status' : 200,
#             'success' : True,
#             'message' : '메시지 전달 성공!',
#             'data' : [
#                 {
#                     # 내 정보
#                     "name" : "정현수",
#                     "age" : 22,
#                     "major" : "LIS"
#                 },
#                 {
#                     # 코드리뷰 짝 정보
#                     "name" : "김동영",
#                     "age" : 24,
#                     "major" : "CSE"
#                 }
#             ]
#         })

# def info_view(request):
#     myinfo_all = myinfo.objects.all()
#     reviewerinfo_all = reviewerinfo.objects.all()
#     return render(request, 'index.html', {'myinfo_list' : myinfo_all, 'reviewerinfo_list': reviewerinfo_all})


# 4주차
# posts
@require_http_methods(["GET"])
def get_post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post_detail_json = {
        "id" : post.id,
        "title" : post.title,
        "content" : post.content,
        "writer" : post.writer,
        "category" : post.category,
    }

    return JsonResponse({
        'status' : 200,
        'message' : '게시글 조회 성공',
        'data' : post_detail_json
    })

#comments
# def get_comment_detail(request, comment_id):
#     comment = get_object_or_404(Comment, pk=comment_id)
#     comment_detail_json = {
#         "id" : comment.id,
#         "comment_id" : comment.comment_id,
#         "commenter" : comment.commenter,
#         "comment" : comment.comment,
#     }

#     return JsonResponse({
#         'status' : 200,
#         'message' : '댓글 조회 성공',
#         'data' : comment_detail_json
#     })


# 5주차
@require_http_methods(["POST", "GET"])
def post_list(request):

    if request.method == "POST":
        # body = json.loads(request.body.decode('utf-8'))

        new_post = Post.objects.create(
            writer = request.POST['writer'],
            title = request.POST['title'],
            content = request.POST['content'],
            image = request.FILES.get('image'), # 추가
            category = request.POST['category']
        )

        new_post_json = {
            "id" : new_post.id,
            "writer" : new_post.writer,
            "title" : new_post.title,
            "content" : new_post.content,
            "image" : new_post.image.url,
            "category" : new_post.category
        }

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 생성 성공',
            'data' : new_post_json
        })
    
    if request.method == "GET":
        post_all = Post.objects.all()

        post_json_all = []

        for post in post_all:
            post_json = {
                "id" : post.id,
                "title" : post.title,
                "writer" : post.writer,
                "contetnt" : post.content,
                # "image" : post.image.url, # 추가
                "category" : post.category
            }
            post_json_all.append(post_json)

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 목록 조회 성공',
            'data' : post_json_all
        })
    

@require_http_methods(["GET", "PATCH", "DELETE"])
def post_detail(request, id):

    if request.method == "GET":
        post = get_object_or_404(Post, pk=id)

        post_json = {
            "id" : post.id,
            "writer" : post.writer,
            "title" : post.title,
            "content" : post.content,
            # "image" : post.image.url, # 추가
            "category" : post.category,
        }

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 조회 성공',
            'data' : post_json
        })
    
    if request.method == "PATCH":
        body = json.loads(request.body.decode('utf-8'))

        update_post = get_object_or_404(Post, pk=id)

        update_post.title = body['title']
        update_post.content = body['content']
        update_post.category = body['category']

        update_post.save()

        update_post_json = {
            "id" : update_post.id,
            "writer" : update_post.writer,
            "title" : update_post.title,
            "content" : update_post.content,
            # "image" : update_post.image.url, # 추가
            "category" : update_post.category,
        }

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 수정 성공',
            'data' : update_post_json 
        })
    
    if request.method == "DELETE":
        delete_post = get_object_or_404(Post, pk=id)
        delete_post.delete()

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 삭제 성공',
            'data' : None
        })
    
# 특정 post의 comment 조회하기 
@require_http_methods(["GET"])
def comment_list(request, id):

    if request.method == "GET":
        comment_all = Comment.objects.filter(post_id_id=id)

        comment_json_all = []

        for comment in comment_all:
            comment_json = {
                "comment_id" : comment.comment_id,
                "commenter" : comment.commenter,
                "comment" : comment.comment,
            }
            comment_json_all.append(comment_json)

        return JsonResponse({
            'status' : 200,
            'message' : '댓글 조회 성공',
            'data' : comment_json_all
        })


# 최근 일주일 동안 작성된 게시글 목록 조회하기
first_date = datetime.date(2024,4,4)
last_date = datetime.date(2024,4,10)

# now = datetime.datetime.now()
# recent_week = now - datetime.timedelta(weeks=1)
# first_date = datetime.date(recent_week.year, recent_week.month, recent_week.day)
# last_date = datetime.date(now.year, now.month, now.day)

@require_http_methods(["GET"])
def recent_post(request, format=None):
    recent_post_all = Post.objects.all().filter(created_at__range=(first_date,last_date)).order_by('-created_at')

    recent_json_all = []

    for post in recent_post_all:
        recent_json = {
            "id" : post.id,
            "date" : post.created_at.strftime('%Y-%m-%d'),
            "writer" : post.writer,
            "title" : post.title,
            "content" : post.content,
            # "image" : post.image.url, #추가
            "category" : post.category,
        }
        recent_json_all.append(recent_json)
        
    return JsonResponse({
            'status' : 200,
            'message' : '최신 게시글 조회 성공',
            'data' : recent_json_all
        })


# 7주차
class PostList(APIView):
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
class PostDetail(APIView):
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        post = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CommentList(APIView):
    def get(self, request, id):
        comment = Comment.objects.filter(post_id=id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)