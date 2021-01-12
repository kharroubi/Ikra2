from django.urls import path

from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path(r'form/', views.form, name='form'),
    path(r'login/', views.login_user, name='login'),
    path(r'logout/', views.logout_user, name='logout'),
]