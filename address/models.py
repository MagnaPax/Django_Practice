from django.db import models


# Create your models here.
# 클래스에 정의한 변수명과 자료형을 기반으로 데이터베이스에 테이블이 만들어진다.

class Address(models.Model):
    # 시퀀스 테이블
    idx = models.AutoField(primary_key=True) # 자동 필드 증가

    name = models.CharField(max_length=50, blank=True, null=False)

    tel = models.CharField(max_length=50, blank=True, null=True)

    email = models.CharField(max_length=50, blank=True, null=True)

    address = models.CharField(max_length=50, blank=True, null=True)
