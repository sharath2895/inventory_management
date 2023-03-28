from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from .views import AddressListView, AddressView


urlpatterns = [
    path('address_list', AddressListView.as_view(), name='address-list'),
    path('address/<int:pk>/', AddressView.as_view(), name='user-address')
]
