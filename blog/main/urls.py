from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path("", TemplateView.as_view(template_name="main/index.html"), name="home_page"),
    path("posts/", views.posts, name="posts"),
    path("posts/create/", views.post_create, name="post_create"),
    path("post/<int:post_id>/", views.post_show, name="post_show"),
    path("post/update/<int:post_id>/", views.post_update, name="post_update"),

    path("authors/new/", views.authors_new, name="authors_new"),
    path("authors/all/", views.authors_all, name="authors_all"),
    path("authors/subscribe/", views.authors_sub, name="authors_sub"),
    path("authors/delete/all/", views.authors_del_all, name="authors_del_all"),

    path("subscribers/all/", views.subscribers_all, name="subscribers_all"),

    path("api/posts/", views.api_posts, name="api_posts"),
    path("api/post/<int:post_id>/", views.api_post_show, name="api_post_show"),
    path("api/subscribe/", views.api_author_subscribe, name="api_subscribe"),
    path("api/subscribers/all/", views.api_subscribers_all, name="api_subscribers_all"),
    path("api/authors/all/", views.api_authors_all, name="api_authors_all"),
    path("api/authors/new/", views.api_authors_new, name="api_authors_new"),

    path("about/", TemplateView.as_view(template_name="main/about.html"), name="about"),
]
