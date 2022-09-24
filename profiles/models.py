from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):

    """
    A user profile model for user information
    and post history record keeking
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder')    
    bio = models.TextField(max_length=250, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    twitter = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User) 
def create_or_update_user_profile(sender, instance, created, **kwargs):

    """
    create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
