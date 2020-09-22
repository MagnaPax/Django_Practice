from django.urls import path
from login import views

urlpatterns = [
    path("", views.main),
    path('loginform', views.loginform),
    path('logout', views.logout),
]
