from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,DetailView
from .models import Post, Comment
from django.urls import reverse_lazy
from user.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required





# Create your views here.

class BlogPostCreateView(CreateView): 
    model = Post 
    fields = ['title', 'text', 'image'] 
    success_url = reverse_lazy('login') 
    template_name = "create-post.html" 

    def form_valid(self, form):
        profile, _ = Profile.objects.get_or_create(id=self.request.user.id)
        form.instance.profile = profile
        return super().form_valid(form)

class MyBlogView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "user-post-list.html"
    context_object_name = "posts"

    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.get(id=user.id)
        return Post.objects.filter(profile=profile)

class BlogPostDetailView(DetailView):
    model = Post
    template_name = "post-detail.html"
    context_object_name = "post"

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=pk)

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    content = request.POST.get('content')
    if content:
        profile = Profile.objects.get(id=request.user.id)
        Comment.objects.create(post=post, author=profile, text=content)
    return redirect('post_detail', pk=pk)