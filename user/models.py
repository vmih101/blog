from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
#     username = None
#     email = models.EmailField(('email address'), unique=True)
#     phone_number = models.CharField(max_length=20, unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    picture = models.ImageField(upload_to='profile_pics/', blank=True)
    # name = models.CharField(max_length=200, blank=True)
    
  
    def __str__(self):
        return str(self.id)


