from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        success_url = '/',
        template_name = 'accounts/login.html',
    ), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page = '/'), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
]
