
from django.contrib import admin
from django.urls import path, include
from address import urls as addressurls
from user import urls as userurls
import djoser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(addressurls)),
    path('user/',include(userurls)),
           
]
