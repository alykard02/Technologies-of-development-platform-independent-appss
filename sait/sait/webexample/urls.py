from django.urls import path
from webexample import views

urlpatterns = [
path('', views.index, name='index'),
]
