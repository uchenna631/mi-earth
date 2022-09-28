from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import EditProfileForm
from blog.forms import AddPostForm
from blog.models import Post


@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_on')
    userprofile = get_object_or_404(UserProfile, user=request.user)
    form = EditProfileForm(
        request.POST or None, request.FILES or None, instance=userprofile)
    if form.is_valid():
        form.save()
        return redirect('profile')
    else:
        form = EditProfileForm(
            request.POST or None, request.FILES or None, instance=userprofile)
    context = {
        'form': form,
        'profile': profile,
        'posts': posts
        }
    return render(request, 'profiles/profile.html', context)

    
@login_required
def add_post(request):
    context = dict(form=AddPostForm())
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = AddPostForm()
    
    return render(request, 'profiles/add_post.html', context)


@login_required
def edit_post(request, slug):
    """
    Edit post function
    """
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, slug=slug)
    form = AddPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'profiles/edit_post.html', {
        'post': post,
        'form': form
    })


@login_required
def delete_post(request, slug):
    """
    Deletes user's post
    """
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('profile')

@login_required()
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    form = EditProfileForm(
        request.POST or None, request.FILES or None, instance=userprofile)
    if form.is_valid():
        form.save()
        return redirect('profile')
    else:
        form = EditProfileForm(
            request.POST or None, request.FILES or None, instance=userprofile)
    context = {
        'form': form,
        'profile': profile,
        }
    return render(request, 'profiles/edit_profile.html', context)