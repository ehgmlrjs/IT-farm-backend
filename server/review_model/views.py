from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from order.models import Review
import re
from django.apps import apps

# 한글과 공백을 제외하고 모두 제거
def preprocess_text(text):
    text = re.sub("[^가-힣\s]", "", text)
    return text

class ReviewPredView(APIView):
    def get(self, request):
        
        optimized_pipeline = apps.get_app_config('review_model').model

        if not optimized_pipeline:
            return Response({'error': 'model 로드 불가'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # 리뷰 추출
        # 모든 리뷰 객체의 content 필드의 쿼리셋 값을 튜플로 반환
        # flat=True : 단일 값의 리스트 반환 
        review_contents = Review.objects.all().values_list('content', flat=True)

        if review_contents:
            predictions = []
            for review_content in review_contents:
                preprocessed_review = preprocess_text(review_content)
                prediction = optimized_pipeline.predict([preprocessed_review])
                predictions.append(prediction[0])
            
            # print([i+1 for i, value in enumerate(predictions) if value == 1])
            
            # 예측 결과 반환
            positive = predictions.count(0)
            negative = predictions.count(1)
            
            return Response({"positive": positive, "negative":negative}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "제공하는 리뷰 없음"}, status=status.HTTP_400_BAD_REQUEST)
