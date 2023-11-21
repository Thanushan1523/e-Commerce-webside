from django.urls import path
from . import views

app_name='dashboard'

urlspatterns = [
    path('',views.index , name='index'),
]

