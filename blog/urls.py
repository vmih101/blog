from django.urls import path
from .views import BlogPostCreateView, MyBlogView, BlogPostDetailView, like_post, add_comment

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='blog_create'),
    path('posts/', MyBlogView.as_view(), name='my_posts'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/like/', like_post, name='like_post'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment')
]