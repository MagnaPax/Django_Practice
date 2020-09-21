from django.db import models
from django import forms
from django.contrib.auth.models import User

# 상품 클래스
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(null=False, max_length=150)

    price = models.IntegerField(default=0)
    description = models.TextField(null=False, max_length=500)
    picture_url = models.CharField(null=True, max_length=150)