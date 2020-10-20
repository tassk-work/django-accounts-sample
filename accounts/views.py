from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from . import forms

class Signup(CreateView):
    form_class = forms.SignupForm
    template_name = 'accounts/signup.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user 
        return redirect(self.get_success_url())

class PasswordChange(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = '/'

    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(self.request, 'Password Changed.')
        return res
