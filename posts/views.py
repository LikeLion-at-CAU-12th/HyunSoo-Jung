from django.shortcuts import render, HttpResponse, render
from django.http import JsonResponse # 추가 
from django.shortcuts import get_object_or_404 # 추가
from .models import myinfo, reviewerinfo
# from .forms import myinfoForm, reviewerinfoForm

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
    
    
def index(request):
    return render(request, 'index.html')


def myinfo_view(request):
    myinfo_all = myinfo.objects.all()
    # if request.method=="POST":
    #     form = myinfoForm(request.form)
    #     if form.is_valid():
    #         form.save()
    # form = myinfoForm()
    return render(request, 'index.html', {"myinfo_list" : myinfo_all}) # 'myinfo_form' : myinfoForm

def reviewerinfo_view(request):
    reviewerinfo_all = reviewerinfo.objects.all()
    # if request.method=="POST":
    #     form = reviewerinfoForm(request.form)
    #     if form.is_valid():
    #         form.save()
    # form = reviewerinfoForm()
    return render(request, 'index.html', {"reviewerinfo_list" : reviewerinfo_all}) #'reviewrinfo_form' : reviewerinfoForm}


def info_view(request):
    myinfo_all = myinfo.objects.all()
    reviewerinfo_all = reviewerinfo.objects.all()
    return render(request, 'index.html', {'myinfo_list' : myinfo_all, 'reviewerinfo_list': reviewerinfo_all})