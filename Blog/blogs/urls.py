from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    
   
    path('login/', auth_views.LoginView.as_view(template_name='blogs/login.html'), name='login'),
    
    
    path('logout/', auth_views.LogoutView.as_view(next_page='blogs:home'), name='logout'),
    
   
    path('new/', views.new_post, name='new_post'),
    
   
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
]