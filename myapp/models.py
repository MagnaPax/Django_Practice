from django.db import models

# Create your models here.


class Post(models.Model):
    # 시퀀스 테이블
    idx = models.AutoField(primary_key=True) # 자동 필드 증가
    title = models.CharField(max_length=50, blank=True, null=False)
    content = models.TextField()
    author = models.TextField()

# class Address(models.Model):
#     # 시퀀스 테이블
#     idx = models.AutoField(primary_key=True)
#
#     name = models.CharField(max_length=50, blank=True, null=False)
#
#     tel = models.CharField(max_length=50, blank=True, null=True)
#
#     email = models.CharField(max_length=50, blank=True, null=True)
#
#     address = models.CharField(max_length=50, blank=True, null=True)