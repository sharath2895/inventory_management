from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
# Create your views here.


class UserListView(generics.GenericAPIView):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request)
        queryset = User.objects.all()
        serializer_data = self.serializer_class(queryset, many=True)
        return Response(data=serializer_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        user_data['role'] = 2
        print(user_data)
        serailizer_data = UserSerializer(data=user_data)
        if serailizer_data.is_valid():
            serailizer_data.save()
            return Response(data=serailizer_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serailizer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, pk):
        data = request.data
        self.pk = pk
        user_data = User.objects.filter(pk=self.pk)
        if not user_data:
            return Response(data={"message": "OOPS! User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer_data = UserSerializer(user_data, many=True)
            return Response(data=serializer_data.data[0], status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = request.data
        user_data = User.objects.filter(pk=pk)
        print(user_data)
        serializer_data = UserSerializer(
            user_data, data, many=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(data=serializer_data.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer_data.errors, status=status.HTTP_404_NOT_FOUND)
