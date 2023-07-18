from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from blog.models import Post

@receiver(pre_save, sender=Post)
def set_profile_id(sender, instance, **kwargs):
    if not instance.profile_id:
        profile = User.objects.get(username=instance.username)
        instance.profile_id = profile.id