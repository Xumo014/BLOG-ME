from django.urls import path
from . import views 
urlpatterns = [
    path('', views.getPosts, name='postall'),
    path("detail/<int:pk>/", views.getPost, name="postdetail"),
    #path("filter/<str:tagname>/", views.getPost, name="post_filter")
    path("about/", views.About, name = "about_me")
]
