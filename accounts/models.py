from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

    @staticmethod # 모델 내부 함수를 사용하는 이유 -> 회고
    def get_user_or_none_by_username(username):
        try:
            return User.objects.get(username=username)
        except Exception:
            return None
        
    # @staticmethod
    # def get_user_or_none_by_email(email):
    #     try:
    #         return User.objects.get(email=email)
    #     except Exception:
    #         return None