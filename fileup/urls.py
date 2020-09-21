from django.urls import path
from fileup import views

urlpatterns = [
    path('', views.main),
    path('upload_success', views.upload_success),
    path('main2', views.main2),
    path('upload_success2', views.upload_success2),
]
