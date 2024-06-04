from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

    @staticmethod
    def get_user_or_none_by_username(username):
        try:
            return User.objects.get(username=username)
        except Exception:
            return None
        
    @staticmethod
    def get_user_or_none_by_email(email):
        try:
            return User.objects.get(email=email)
        except Exception:
            return None
        
# class SocialAccount(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     provider = models.CharField(max_length=255)
#     uid = models.CharField(max_length=255)
#     extra_data = models.JSONField(default=dict)

#     def __str__(self):
#         return f'{self.user} - {self.provider}'