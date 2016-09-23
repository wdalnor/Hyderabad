from django import forms
from .models import Notification
from django.contrib.auth.models import User


class notificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ('title', 'message', 'attach', 'viewed','user' )


class UserForm(forms.ModelForm):


    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:

        model = User
        fields = ('username', 'email', 'password')

