from django.db import models
from product.models import Product

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=45)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # product_id 
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0) # 0이면 결제 전 
    count = models.IntegerField()

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE) # order_number 
    product_id = models.IntegerField()
    nickname = models.CharField(max_length=45)
    content = models.TextField()
    photo = models.CharField(max_length=255, null=True)
    score = models.IntegerField()
    kind = models.CharField(max_length=45)
    regdate = models.DateTimeField(auto_now_add=True)