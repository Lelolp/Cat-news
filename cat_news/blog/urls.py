"""
URL configuration for cat_news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from .views import posts, generate_new_post
from .views import about_us
from .views import post_detail

urlpatterns = [
    path('', posts,name="posts"),
    path('about-us/', about_us,name="about-us"),
    path('posts/<int:post_id>/',post_detail,name="post-detail"),
    path('posts/generate-new/',generate_new_post,name="generate-new-post"),
]
