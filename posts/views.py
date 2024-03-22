from django.shortcuts import render, HttpResponse, render
from django.http import JsonResponse # 추가 
from django.shortcuts import get_object_or_404 # 추가
from .models import myinfo, reviewerinfo
from .forms import myinfoform, reviewerinfoform

# Create your views here.
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
                    "major" : "LIS",
                    "git": "@usernamehs"
                },
                {
                    # 코드리뷰 짝 정보
                    "name" : "김동영",
                    "age" : 24,
                    "major" : "CSE",
                    "git" : "@Temple2001"
                }
            ]
        })
    
    
def index(request):
    return render(request, 'index.html')


def myinfo_view(request):
    myinfo_all = myinfo.objects.all()
    return render(request, 'index.html', {"myinfo_list" : myinfo_all})

def reviewerinfo_view(request):
    reviewerinfo_all = reviewerinfo.objects.all()
    return render(request, 'index.html', {"reviewer_list" : reviewerinfo_all})