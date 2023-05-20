from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('results/<poll_id>/', results, name='results'),
    path('vote/<poll_id>/', vote, name='vote'),
    path('delete/<poll_id>/<str:action>/', vote, name='delete-view'),
]

    
    