from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User

urlpatterns = [
    # 방명록 생성, 조회, 삭제
    path('', GuestBookPost.as_view()),
    path('<int:pk>/', GuestBookGet.as_view()),
    path('<int:pk>/delete/', GuestBookDelete.as_view()),
    # 방명록 리스트 조회
    path('list/', GuestBookList.as_view()),
    path('list/sort/', GuestBookListSort.as_view()),
]