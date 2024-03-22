from django.db import models

# Create your models here.
class myinfo(models.Model):
    myname = models.CharField(default="", max_length = 10)
    myage = models.IntegerField(default=0)
    mymajor = models.CharField(default="", max_length = 50)
    mygit = models.CharField(default="", max_length = 15)

class reviewerinfo(models.Model):
    reviewername = models.CharField(default="", max_length = 10)
    reviewerage = models.IntegerField(default=0)
    reviewermajor = models.CharField(default="", max_length = 50)
    reviewergit = models.CharField(default="", max_length = 15)
