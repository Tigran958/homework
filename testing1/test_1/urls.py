from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),

]