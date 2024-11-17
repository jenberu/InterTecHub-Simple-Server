
from django.contrib import admin
from django.urls import path,include
from message import views



urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('message/',include('message.urls')),#include the message urls
]
