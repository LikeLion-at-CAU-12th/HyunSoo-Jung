from django.db import models

# Create your models here.

# 3주차 모델
# class myinfo(models.Model):
#     myname = models.CharField(default="", max_length = 10)
#     myage = models.IntegerField(default=0)
#     mymajor = models.CharField(default="", max_length = 50)
#     mygit = models.CharField(default="", max_length = 15)

# class reviewerinfo(models.Model):
#     reviewername = models.CharField(default="", max_length = 10)
#     reviewerage = models.IntegerField(default=0)
#     reviewermajor = models.CharField(default="", max_length = 50)
#     reviewergit = models.CharField(default="", max_length = 15)


# 4주차 모델
class Hashtag(models.Model):
    tag = models.TextField(unique=True, max_length=100)
    
    def __str__(self):
      return str(self.tag)

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True

class Post(BaseModel):
    CHOICES = (
        ('DAIRY', '일기'),
        ('STUDY', '공부'),
        ('ETC', '기타')
    )

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=20)
    content = models.TextField(verbose_name="내용")
    writer = models.CharField(verbose_name="작성자", max_length=10, null=False)
    category = models.CharField(choices=CHOICES, max_length=20)
    # image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True) # 추가
    tag = models.ManyToManyField(Hashtag, blank=True)


class Comment(BaseModel):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_id = models.AutoField(primary_key=True)
    # user_id = 
    commenter = models.CharField(verbose_name="댓글작성자", max_length=10)
    comment = models.TextField(verbose_name="댓글내용", max_length=500)

    def __str__(self):
        return str(self.commenter)