from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
User = get_user_model()

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    full_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['full_name','username', 'email',  'phone_number', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash password
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )



from django import forms
from .models import AgroBusiness

class AgroBusinessForm(forms.ModelForm):
    class Meta:
        model = AgroBusiness
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'benefits': forms.Textarea(attrs={'rows': 3}),
            'loss': forms.Textarea(attrs={'rows': 2}),
            'side_business': forms.Textarea(attrs={'rows': 2}),
        }


from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'full_name',
            'email',
            'is_first_time',
            'reason',
            'found_what_needed',
            'user_friendliness'
        ]
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Why did you visit the site?'}),
            'user_friendliness': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
        labels = {
            'is_first_time': 'Is this your first time visiting the website?',
            'found_what_needed': 'Did you find what you needed?',
            'user_friendliness': 'User Friendliness (1 to 5)',
        }