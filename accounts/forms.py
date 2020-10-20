from django.contrib.auth import forms as auth_forms
from django.contrib.auth import models as auth_models

class SignupForm(auth_forms.UserCreationForm):
    class Meta:
        model = auth_models.User
        fields = ('username', 'password1', 'password2')