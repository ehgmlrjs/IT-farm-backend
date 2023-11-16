from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False) # 작물명
    kind = models.CharField(max_length=100,default='고추') # 품종
    count = models.IntegerField(default=0,null=False) # 수량
    price = models.IntegerField(null=False) # 가격
    photo = models.CharField(max_length=100,null=True) # 사진