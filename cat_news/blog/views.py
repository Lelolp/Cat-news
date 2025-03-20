from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from .GPT_gen import PostGenerator

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request,"blog/posts.html",context={"posts":posts})
def about_us(request):
    return render(request,"blog/about_us.html")
def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)
    return render(request,"blog/post_detail.html",context={"post":post})
def generate_new_post(request):
    generator = PostGenerator()
    post_data = generator.generate_news_post()
    post = Post.objects.create(title=post_data['title'],
                               content=post_data['text'],
                               picture=post_data['image'])
    post.save()
    return HttpResponse("Post generated successfully")