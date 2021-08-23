from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('priv', views.private_page, name='priv'),
    path('pub', views.public_page, name='pub'),
    path('signup/', SignUpView.as_view(), name='singup')
]