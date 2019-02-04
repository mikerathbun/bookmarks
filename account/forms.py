from django import forms


class LoginForm(forms.Form):
    """form class for the login form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
