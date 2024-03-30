from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from posts.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

# 3주차
def hello_world(request):
    if request.method == "GET":
        return JsonResponse({
            'status' : 200,
            'success' : True,
            'message' : '메시지 전달 성공!',
            'data' : [
                {
                    # 내 정보
                    "name" : "정현수",
                    "age" : 22,
                    "major" : "LIS"
                },
                {
                    # 코드리뷰 짝 정보
                    "name" : "김동영",
                    "age" : 24,
                    "major" : "CSE"
                }
            ]
        })

def info_view(request):
    myinfo_all = myinfo.objects.all()
    reviewerinfo_all = reviewerinfo.objects.all()
    return render(request, 'index.html', {'myinfo_list' : myinfo_all, 'reviewerinfo_list': reviewerinfo_all})


# 4주차
# # posts
# @require_http_methods(["GET"])
# def get_post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     post_detail_json = {
#         "post_id" : post.post_id,
#         "title" : post.title,
#         "content" : post.content,
#         "writer" : post.writer,
#         "category" : post.category,
#     }

#     return JsonResponse({
#         'status' : 200,
#         'message' : '게시글 조회 성공',
#         'data' : post_detail_json
#     })

# #comments
# def get_comment_detail(request, comment_id):
#     comment = get_object_or_404(Comment, pk=comment_id)
#     comment_detail_json = {
#         "post_id" : comment.post_id,
#         "comment_id" : comment.comment_id,
#         "commenter" : comment.commenter,
#         "comment" : comment.comment,
#     }

#     return JsonResponse({
#         'status' : 200,
#         'message' : '댓글 조회 성공',
#         'data' : comment_detail_json
#     })