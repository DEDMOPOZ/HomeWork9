from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .authors_services import authors, delete_all_authors, new_author
from .form import CommentForm, PostForm, SubscribeForm
from .models import Author, Post
from .post_services import post_all, post_find
from .subsribers_services import sub_all


def posts(request):
    return render(request, "main/posts.html", {"title": "Posts", "posts": post_all()})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "main/post_create.html", context=context)


def post_show(request, post_id):
    post = post_find(post_id)
    comments = post.comments.all()

    new_comment = None

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(request.META.get("HTTP_REFERER"))
    else:
        form = CommentForm()
    context = {
        "form": form,
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
    }
    return render(request, "main/post_show.html", context=context)


def post_update(request, post_id):
    pst = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm(instance=pst)
    context = {
        "form": form,
    }
    return render(request, "main/post_update.html", context=context)


def authors_new(request):
    new_author()
    return redirect("authors_all")


def authors_all(request):
    return render(request, "main/authors.html", {"title": "Authors", "authors": authors()})


def authors_sub(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subscribers_all")
    else:
        form = SubscribeForm()
    context = {
        "form": form,
    }
    return render(request, "main/authors_subscribe.html", context=context)


def authors_del_all(request):
    delete_all_authors()
    return redirect("authors_all")


def subscribers_all(request):
    return render(request, "main/subscribers.html", {"title": "Subscribers", "subscribers": sub_all()})


def api_posts(request):
    all_posts = post_all()
    posts_list = list(all_posts.values())
    return JsonResponse(posts_list, safe=False)


def api_post_show(request, post_id):
    post = post_find(post_id)
    data = {
        "post_title": post.title,
        "post_description": post.description,
        "post_content": post.content
    }
    return JsonResponse(data, safe=False)


def api_author_subscribe(request):
    author_id = request.GET.get("author_id")
    email_to = request.GET("email_to")
    data = {"author_id": author_id, "email_to": email_to}
    return JsonResponse(data, safe=False)


def api_subscribers_all(request):
    all_subs = sub_all()
    subs_list = list(all_subs.values())
    return JsonResponse(subs_list, safe=False)


def api_authors_all(request):
    all_authors = authors()
    authors_list = list(all_authors.values())
    return JsonResponse(authors_list, safe=False)


def api_authors_new(request):
    new_author()
    author = Author.objects.last()
    data = {
        "author_id": author.id,
        "author_name": author.name,
        "author_email": author.email
    }
    return JsonResponse(data, safe=False)
