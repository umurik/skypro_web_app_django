from django.urls import path

from .views import contacts, home

urlpatterns = [
    path("", home),
    path("contacts/", contacts),
]
