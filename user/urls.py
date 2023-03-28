from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from .views import UserListView, UserView


urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserView.as_view(), name='user-detail'),
    path('auth/',include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
