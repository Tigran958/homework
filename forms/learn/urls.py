from django.urls import path
from . import views


urlpatterns = [

    # path('1', views.get_name, name='get_name'),
    path('get_name', views.get_name, name='get_name'),
        
]