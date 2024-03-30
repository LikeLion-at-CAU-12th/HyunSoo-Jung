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

urlpatterns = [
    path('', index),
    path('introduction', hello_world, name = 'hello_world'),
    # path('index', index, name='my-page'),
    # path('page', info_view),
    path('post<int:post_id>', get_post_detail, name = "게시글 조회"),
    # path('comment<comment_id>', get_comment_detail, name = "댓글 조회")
]
