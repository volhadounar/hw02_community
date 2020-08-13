from django.urls import path

from . import views

#https://docs.djangoproject.com/en/3.0/ref/urls/#django.urls.path
urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug:slug>", views.group_posts),
]