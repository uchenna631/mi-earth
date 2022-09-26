from django import forms
from .models import UserProfile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'user',
            'email',
            'twitter',
            'profile_image',
            'bio',
         )
        widgets = {
            'user': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
                 }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
                 }),
            'twitter': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Twitter username'
                 }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                "rows": 3,
                "cols": 20,
                'placeholder': 'Say something about yourself'
                }),
            
                    }
