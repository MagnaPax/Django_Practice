"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from survey import views

urlpatterns = [
    # 주소창에 http://localhost/survey/ 입력되면 views 파일 안의 home 메소드를 읽어라.
    # home 메소드 안에는 list.html 을 읽으라고 되어있음
    # http://localhost/survey/ ==> views.home() ==> templates/survey/list.html
    path('', views.home),

    # http://localhost/survey/save_survey ==> views.save_survey() ==> templates/survey/success.html
    path('save_survey', views.save_survey),

    # http://localhost/survey/show_result ==> views.show_result() ==> templates/survey/result.html
    path('show_result', views.show_result),
]
