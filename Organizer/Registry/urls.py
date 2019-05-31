from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('login/', views.login, name = 'login'),
        path('home/', views.loginHome, name = 'home'),
        path('home/', views.logout, name="logout"),
        path('signup/', views.register, name='home'),
]
