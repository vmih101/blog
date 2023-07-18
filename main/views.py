from django.shortcuts import render
from blog.models import Post

# Create your views here.

def post_like(request):
    link = Post.objects.filter(likes__gt = 0)
    print(link)
    return render(request, "main.html",{'link':link})
