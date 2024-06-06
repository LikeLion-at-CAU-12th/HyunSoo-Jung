"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from posts.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User

urlpatterns = [
    # path('', index),
    # path('introduction', hello_world, name = 'hello_world'),
    # # path('index', index, name='my-page'),
    # # path('page', info_view),
    # path('<int:post_id>', get_post_detail, name = "게시글 조회"),
    # path('<int:comment_id>/comment', get_comment_detail, name = "댓글 조회"),
    # path('<int:tag_id>/hashtag', hashtag, name = "해시태그"),
    
    # path('', post_list, name="post_list"),
    # path('<int:id>/', post_detail, name="post_detail"),
    # path('<int:id>/comment', comment_list, name="comment_list"),
    # path('recent/', recent_post, name="recent_post"),

    path('', PostList.as_view()),
    path('<int:id>/', PostDetail.as_view()),
    path('<int:id>/comment/', CommentList.as_view()),
    # path('', PostListGenericAPIView.as_view()),
    # path('<int:post_id>/', PostDetailGenericAPIView.as_view())
]

# media 경로 추가
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)