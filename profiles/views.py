from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from blog.models import Post
from .forms import EditProfileForm


def profile(request):
    """
    Create profile view
    """
    user = request.user
    posts = Post.objects.filter(author=user)
    user_profile = UserProfile.objects.get(user=user)
    form = EditProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=user_profile
    )
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'posts': posts

    }
    return render(request, 'profile.html', context)
    
