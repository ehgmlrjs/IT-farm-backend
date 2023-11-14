from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Notice
from .serializers import NoticeSerializer
from django.db.models import Q

class NoticeReadView(APIView):
    def post(self, request):
        notice_type = int(request.data.get('notice_type', 0))
        user_type = request.data.get('user_type')

        # 0: 노하우 1: 공지
        if notice_type == 0 and user_type.lower() == 'seller':
            notices = Notice.objects.filter(notice_type=0)
        elif notice_type == 1 and user_type.lower() == 'buyer':
            notices = Notice.objects.filter(notice_type=1, user_type='buyer')
        elif notice_type == 1 and user_type.lower() == 'seller':
            notices = Notice.objects.filter(notice_type=1, user_type='seller')
        elif notice_type == 0 and user_type.lower() == 'admin':
            notices = Notice.objects.filter(notice_type=0)
        elif notice_type == 1 and user_type.lower() == 'admin':
            notices = Notice.objects.filter(notice_type=1)
        else:
            return Response({"error": "Invalid parameters"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NoticeDetailReadView(APIView):
    def post(self,request):
        pk = request.data.get('notice_id')
        notices = Notice.objects.filter(notice_id=pk)
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NoticeCreateView(APIView):
    def post(self, request):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NoticeUpdateView(APIView):
    def post(self, request):
        pk = request.data.get('notice_id')
        notice = get_object_or_404(Notice, notice_id=pk)
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoticeDeleteView(APIView):
    def post(self, request):
        pk = request.data.get('notice_id')
        notice = get_object_or_404(Notice, notice_id=pk)
        try:
            notice.delete()
            return Response({'message': '삭제'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': '실패'}, status=status.HTTP_400_BAD_REQUEST)
    
class NoticeSearchView(APIView):
    def post(self, request):
        search = request.data.get('search', '')

        if search:
            search_list = Notice.objects.filter(
                Q(subject__icontains=search) |
                Q(content__icontains=search)
            )
        else:
            search_list = Notice.objects.all()
        
        serializer = NoticeSerializer(search_list, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
