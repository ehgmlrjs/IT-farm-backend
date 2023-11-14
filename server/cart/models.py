from django.db import models
from product.models import Product

class Cart(models.Model):
    user_id = models.IntegerField(null=False) # 유저 id
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id') # 상품 id
    count = models.IntegerField(default=0, null=False) # 수량
    created_at = models.DateTimeField(auto_now_add=True) # 등록일자
    updated_at = models.DateTimeField(auto_now=True) # 수정일자