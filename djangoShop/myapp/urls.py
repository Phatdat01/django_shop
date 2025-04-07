from django.urls import path
from . import views

#Define a list url patterns
urlpatterns = [
    path('', views.index)
]