from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    """
    Register user profile to admin
    """
    list_display = ('user', 'profile_image', 'bio', 'email', 'twitter')
    search_fields = ['user', 'email']

