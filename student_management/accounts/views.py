from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,AllowAny


class RegisterUser(APIView):
    permission_classes = [AllowAny]
    def post(self,request):

        serializer=RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'user created successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user=request.user
        serializer=UserSerializer(user)
        return Response(serializer.data)


class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data['refresh']
            token=RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message':'user logged out successfully'},status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)





