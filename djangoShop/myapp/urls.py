from django.urls import path, include
from . import views

#Define a list url patterns
urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.home_view, name="home"),
    path('contact/', views.contact_view, name="contact"),
    path('contact/success', views.contact_success_view, name="contact-success"),
]