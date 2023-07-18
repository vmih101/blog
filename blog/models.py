from django.urls import reverse
from django.db import models
from user.models import Profile
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    image = models.ImageField(upload_to = 'images/')
    created = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    


    def __str__ (self):
        return str(self.title) + str(self.created)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text