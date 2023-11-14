# CRUD + 검색 + 댓글 
from rest_framework import serializers
from .models import Qna, Comment

class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qna
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# qna_id 필요없을것같아서 
class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id', 'content')