from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import AddressSerializer
from .models import Address
from user.models import User
# Create your views here.

# address list


class AddressListView(generics.GenericAPIView):
    # permission_classes = IsAuthenticated
    serializer_class = Address.objects.all()

    def get_queryset(self):
        return self.serializer_class

    def get(self, request):
        address_list = self.get_queryset()
        serializer_data = AddressSerializer(address_list, many=True)
        return Response(data=serializer_data.data, status=status.HTTP_200_OK)


class AddressView(generics.GenericAPIView):

    serializer_class = Address.objects.all()

    def get(self, request, pk):
        user_address = Address.objects.filter(user_id=pk)
        serializer_data = AddressSerializer(user_address, many = True)
        if not user_address:
            return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=serializer_data.data, status=status.HTTP_200_OK)
