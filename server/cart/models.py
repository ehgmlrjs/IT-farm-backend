from django.db import models
from product.models import Product

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=False) # 유저 id
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_name', to_field='name') # 상품 id
    count = models.IntegerField(default=0, null=False) # 수량
    created_at = models.DateTimeField(auto_now_add=True) # 등록일자