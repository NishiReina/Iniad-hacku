from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.top),
    path(r'search', views.search)
]