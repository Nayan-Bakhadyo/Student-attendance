from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.login1,name='login'),
    path('signup/', views.signup,name='signup'),
    path('signout/', views.signout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('detection/', views.detection, name='detection'),
    path('dataset/', views.dataset, name='dataset'),
    path('dashboard/', views.dashboard, name='dashboard'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)