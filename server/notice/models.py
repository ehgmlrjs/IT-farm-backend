from django.db import models

class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    regdate = models.DateField(auto_now_add=True)