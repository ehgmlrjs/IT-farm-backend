from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Notice
from .serializers import NoticeSerializer
from django.db.models import Q

class NoticeReadView(APIView):
    def get(self, request):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NoticeDetailReadView(APIView):
    def get(self, request, notice_id):
        notices = Notice.objects.filter(notice_id=notice_id)
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
    def put(self, request):
        pk = request.data.get('notice_id')
        notice = get_object_or_404(Notice, notice_id=pk)
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoticeDeleteView(APIView):
    def delete(self, request, notice_id):
        notice = get_object_or_404(Notice, notice_id=notice_id)
        try:
            notice.delete()
            return Response({'message': '삭제'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': '실패'}, status=status.HTTP_400_BAD_REQUEST)
    
class NoticeSearchView(APIView):
    def get(self, request):
        search = request.query_params.get('search')

        if search:
            search_list = Notice.objects.filter(
                Q(subject__icontains=search) |
                Q(content__icontains=search)
            )
        else:
            search_list = Notice.objects.all()
        
        serializer = NoticeSerializer(search_list, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
