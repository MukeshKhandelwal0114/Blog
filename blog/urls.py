from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_views, name='login'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('logout/', views.logout_views, name='logout'),
    
]