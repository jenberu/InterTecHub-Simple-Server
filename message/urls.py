from django.urls import path 
from . import views


urlpatterns = [
    path('name/', views.my_name, name='name'),
    path('hobby/', views.my_hobby, name='hobby'),
    path('dream/', views.my_dream, name='dream'),
]