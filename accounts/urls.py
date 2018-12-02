from django.urls import path
from accounts import views


urlpatterns = [
    path('logint', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
