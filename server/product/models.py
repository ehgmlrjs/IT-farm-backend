from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True) # 작물명
    kind = models.CharField(max_length=100,default='고추') # 품종
    count = models.IntegerField(default=0,null=False) # 수량
    price = models.IntegerField(null=False) # 가격
    photo = models.CharField(max_length=100,null=True) # 사진