from django.urls import path, include
from .api import RegisterAPI, loginAPI, UserAPI, ChangePasswordView
from knox import views as knox_views
from users import views as auth_views
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path(r'api/auth', include('knox.urls')),
    path(r'api/auth/register', RegisterAPI.as_view()),
    path(r'api/auth/login', loginAPI.as_view()),
    path(r'api/auth/user', UserAPI.as_view()),
    path(r'api/passwordchange/', ChangePasswordView.as_view()),
    path(r'api/auth/logout', knox_views.LogoutView.as_view(), name='knoxlogout'),
    # path(r'api/password_reset', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path(r'api/password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),
    path(r'api/password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path(r'api/password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'api/password_reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path(r'api/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path(r'api/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    ]