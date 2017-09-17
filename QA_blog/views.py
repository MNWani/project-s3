# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib.auth import login, authenticate
from QA_blog.forms import SignUpForm
from django.shortcuts import redirect
from QA_blog.models import Article
from QA_blog.models import Video



def home(request):
    return render(request, "home.html")


def reviews(request):
    return render(request, "reviews.html")


def reviewsdetail(request):
    return render(request, "blogs/reviewsdetail.html")


def qa_corner(request):
    return render(request, "qa_corner.html")


def post_list(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to my '.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogs/blogposts.html", {'posts': posts})


def post_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post = get_object_or_404(Post, pk=id)
    post.views += 1  # displays the number of post views
    post.save()
    return render(request, "blogs/postdetail.html", {'post': post})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def article(request):
    article_info = Article.objects.all()
    context = {'article_info': article_info}
    return render(request, 'reviews.html', context)


def article_detail(request, id):
    details = get_object_or_404(Article, pk=id)
    context = {'article_info': [details]}
    return render(request, 'reviews.html', context)


def post_article_detail(request, id):
    detail = get_object_or_404(Article, pk=id)
    detail.save()
    return render(request, "blogs/reviewsdetail.html", {'detail': detail})


def videos(request):
    video_info = Video.objects.all()
    context = {'video_info': video_info}
    return render(request, "qa_corner.html", context)


def get_video(request, id):
    vid = get_object_or_404(Video, pk=id)
    context = {'vid': vid}
    return render (request, "qa_corner.html", context)

