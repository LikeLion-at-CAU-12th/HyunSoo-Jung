from django.shortcuts import render
from django.http import JsonResponse # 추가 
from django.shortcuts import get_object_or_404 # 추가

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