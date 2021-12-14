from django.urls import path
from . import views
from landing.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login-user', views.login_user, name='login_user'),
]