from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blogHome, name='BlogHomePage'),
    path('c',views.postComment,name='postCommentAPI'), # API for posting comments
    path('<str:slug>', views.blogPost, name='BlogPostPage'),
]