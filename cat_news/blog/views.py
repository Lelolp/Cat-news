from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request,"blog/posts.html",context={"posts":posts})
def about_us(request):
    return render(request,"blog/about_us.html")
def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)
    return render(request,"blog/post_detail.html",context={"post":post})