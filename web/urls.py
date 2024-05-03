"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import *
from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detail/<int:id>/', detail, name='single-post'), 
    path('create_category/', CreateCategory, name='create_category'),
    path('user_register/', user_register, name ='create_user'),
    path('comment<int:id>/', createComment, name='comment'),
    path('news/create/', createNews, name='create_news'),
    path('delete/<int:id>/', delete, name='ochirish'),
    path('editnews/<int:id>/', editnews, name='editnews'),
    path('password/edit/', password_edit, name='password_edit'),
    path('user_edit/', user_edit, name='user_edit'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('delet/<int:id>/', delete_comment, name='delet')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

