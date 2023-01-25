from django.urls import path,include

from review.views import accom, home, post,post_search,createPost

urlpatterns = [
    path('',home,name="index"),
    path('accom/<str:slug>/',accom,name="accom"),
    path('<str:slug>/post/',post,name="post"),
    path('search/',post_search,name="search"),
    path('post/create/<str:slug>/',createPost,name="create"),




]