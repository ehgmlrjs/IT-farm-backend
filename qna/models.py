from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Qna(models.Model):
    qna_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=25)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    regdate = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0) # 답변 완료(1) 답변 미완료(0)
    user_type = models.CharField(max_length=25)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    qna = models.ForeignKey(Qna, on_delete=models.CASCADE)
    content = models.TextField()
    regdate = models.DateTimeField(auto_now_add=True)

# 댓글 달릴 때 Qna status 0에서 1로 수정
@receiver(post_save, sender=Comment)
def update_qna(sender, instance, created, **kwargs):
    if created:
        qna = instance.qna
        qna.status = 1
        qna.save()
