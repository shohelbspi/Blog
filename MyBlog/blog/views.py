from django.shortcuts import render
from blog.models import Post

# Create your views here.

def blogpost(request):
    allPosts = Post.objects.all()
    params = {'posts':allPosts}
    return render(request,'blog/blog.html',params)


def blogdetails(request,slug):
    post = Post.objects.filter(slug=slug).first()
    params = {'post':post}
    return render(request,'blog/blogdetails.html',params)

