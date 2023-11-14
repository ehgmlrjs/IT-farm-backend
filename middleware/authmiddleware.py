import jwt
from users.serializers import *
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from first_app.my_settings import SECRET_KEY

# 토큰 검증
class Authmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        urls = ('/users/','/product/read/','/product/detail/','/product/search/','/event/read/','/recipe/read/',
                '/redipe/detail/','/recipe/search/')
        if request.path in urls:
            response = self.get_response(request)
            return response
        
        if request.path.startswith('/users/'):
            response = self.get_response(request)
            return response
        
        try:
            access = request.COOKIES.get('access_token')
            payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
            pk = payload.get('user_id')
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(instance=user)
            request.member = serializer.data
            response = self.get_response(request)
            return response

        except(jwt.exceptions.ExpiredSignatureError):
            refresh = request.COOKIES.get('refresh_token')
            data = {'refresh': refresh}
            serializer = TokenRefreshSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                access = serializer.validated_data['access']
                payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_object_or_404(User, pk=pk)
                serializer = UserSerializer(instance=user)
                request.user = serializer.data
                response = self.get_response(request)
                response.set_cookie('access_token', access, httponly=True, secure=True, max_age=3600)
                return response
            else:
                raise jwt.exceptions.InvalidTokenError

        except(jwt.exceptions.InvalidTokenError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        