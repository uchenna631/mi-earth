from django import forms
from .models import UserProfile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'full_name',
            'email',
            'twitter',
            'profile_image',
            'bio',
         )
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
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
