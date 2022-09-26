from django.shortcuts import render
from .forms import EditProfileForm


def profile(request):
    form = EditProfileForm()
    context = {
        'form': form,

    }
    return render(request, 'profile.html', context)
    