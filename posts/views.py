from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from posts.models import *

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
def get_post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_detail_json = {
        "post_id" : post.post_id,
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


# 5주차
@require_http_methods(["POST", "GET"])
def post_list(request):

    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))

        new_post = Post.objects.create(
            writer = body['writer'],
            title = body['title'],
            content = body['content'],
            category = body['category']
        )

        new_post_json = {
            "id" : new_post.post_id,
            "writer" : new_post.writer,
            "title" : new_post.title,
            "content" : new_post.content,
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
                "id" : post.post_id,
                "title" : post.title,
                "writer" : post.writer,
                "contetnt" : post.content,
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
            "id" : post.post_id,
            "writer" : post.writer,
            "title" : post.title,
            "content" : post.content,
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
            "id" : update_post.post_id,
            "writer" : update_post.writer,
            "title" : update_post.title,
            "content" : update_post.content,
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