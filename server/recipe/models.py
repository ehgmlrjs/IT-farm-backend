from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.CharField(max_length=255, null=True)
    regdate = models.DateTimeField(auto_now_add=True)