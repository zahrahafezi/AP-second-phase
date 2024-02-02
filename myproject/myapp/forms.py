from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Userrole


class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'example@gmail.com'}))
    first_name = forms.CharField(label='First Name', max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(label='Last Name', max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    role = forms.ChoiceField(choices=Userrole.ROLE_CHOICES, label='Role')

    class Meta:
        model = Userrole
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['role'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[('patient', 'patient'), ('secretary', 'secretary')])
