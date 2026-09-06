from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import contact
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter your password'})

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ("contact_name", 'contact_email', 'contact_subject', 'project_type', 'contact_message')
        
        widgets = {
                'contact_name': forms.TextInput(attrs={'placeholder': "Enter your name"}),
                'contact_email': forms.EmailInput(attrs={'placeholder': "Enter your email"}),
                'contact_subject': forms.TextInput(attrs={'placeholder': "Enter your subject"}),
                'project_type': forms.Select(choices=[
                    ('', 'Select project type'),
                    ('Web Application', 'Web Application'),
                    ('Backend Development', 'Backend Development'),
                    ('API Development', 'API Development'),
                    ('Other', 'Other'),
                ]),
                'contact_message': forms.Textarea(attrs={'placeholder': "Enter your message"})
            }
    

