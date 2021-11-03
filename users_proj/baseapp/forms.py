from django import forms
from django.contrib.auth.models import User
from baseapp.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields =  ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('user_site', 'user_pic')
