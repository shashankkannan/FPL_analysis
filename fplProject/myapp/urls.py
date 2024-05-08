from django.contrib import admin
from django.urls import path, include

from myapp import views

app_name = 'myapp'

urlpatterns = [
path('',views.show,name='show')
]