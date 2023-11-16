from django.db import models
from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    # nickname = models.CharField(max_length=45)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE) # product_id 
    user_id = models.ForeignKey(User, ondelete=models.CASCADE, db_column='user_id')
    product = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0) # 0이면 결제 전 
    mail_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    address_detail = models.CharField(max_length=100)
    count = models.IntegerField()
    center = models.CharField(max_length=45)

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE) # order_number 
    product_id = models.IntegerField()
    nickname = models.CharField(max_length=45)
    content = models.TextField()
    photo = models.CharField(max_length=255, null=True)
    score = models.IntegerField()
    regdate = models.DateTimeField(auto_now_add=True)

# 리뷰 달릴 때 order status 0에서 1로 수정
@receiver(post_save, sender=Review)
def update_qna(sender, instance, created, **kwargs):
    if created:
        order = instance.order
        order.status = 1
        order.save()