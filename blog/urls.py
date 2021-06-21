from django.urls import path

from blog.views import index, post

urlpatterns = [
    path('', index),
    path('post/', post, name="post")
]
