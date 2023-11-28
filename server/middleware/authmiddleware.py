import jwt
from users.serializers import *
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from first_app.my_settings import SECRET_KEY

# 토큰 검증
class Authmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        allowed_paths = ('/users/','/admin/','/product/detail/','/order/review/read/','/recipe/read/','/review_model/')
        if any(request.path.startswith(path) for path in allowed_paths):
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

        except jwt.exceptions.ExpiredSignatureError:
            refresh = request.COOKIES.get('refresh_token')
            data = {'refresh': refresh}
            serializer = TokenRefreshSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                access = serializer.validated_data['access']
                payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_object_or_404(User, pk=pk)
                serializer = UserSerializer(instance=user)
                request.member = serializer.data
                response = self.get_response(request)
                response.set_cookie('access_token', access, httponly=True, secure=False)
            else:
                raise jwt.exceptions.InvalidTokenError

        except jwt.exceptions.InvalidTokenError:
            response = JsonResponse({'message':'로그인 x'},status=status.HTTP_401_UNAUTHORIZED, content_type="application/json")
        
        except Exception as e:
            print(f"An exception accurred: {e}")
            response = JsonResponse(status=status.HTTP_401_UNAUTHORIZED)
        
        return response
