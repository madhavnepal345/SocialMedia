from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view




urlpatterns = [
    path('login/',user_login, name='login'),
    path('logout/',user_logout,name='logout'),
    path('password_change/',auth_view.PasswordChangeView.as_view(template_name='password_change_form.html'),
         name='password_change'),
    
]


