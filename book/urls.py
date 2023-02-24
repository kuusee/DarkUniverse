from django.urls import include, path
from .views import Home, Post, about


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("search/", Home.as_view(), name="search"),
    path("about/", about, name="about"),
    path("post/<int:post_id>/", Post.as_view(), name="post"),
    path("__debug__/", include("debug_toolbar.urls")),
]
