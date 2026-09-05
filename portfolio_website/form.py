from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import contact
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter your password'})

class ContactForm(forms.ModelForm):
    model = contact
    fields = ("name", 'email', 'subject', 'project_type', 'message')

    widgets = {
        'name': forms.TextInput(attrs={'class': "form-group" ,"placeholder": "Enter your name"}),
        'email': forms.TextInput(attrs={'class': "form-group" ,"placeholder": "Enter your email"}),
        'subject': forms.TextInput(attrs={'class': "form-group" ,"placeholder": "Enter your subject"}),
        'project_type': forms.Select(attrs={'class': "form-group"}),
        'message': forms.Textarea(attrs={'class': "form-group" ,"placeholder": "Enter your message"})
    }

