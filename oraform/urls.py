from django.contrib import admin
from django.urls import path

from oraform import views

urlpatterns = [
    # 주소창에 http://localhost/oraform/main 입력되면 views.py 파일 안의 index 메소드를 읽어라.
    # http://localhost/oraform/main ==> views.index() ==> index.html
    path('main', views.index, name='main'),

    # 주소창에 http://localhost/oraform/tripmember 입력되면 views.py 파일 안의 tripmember 메소드를 읽어라.
    path('tripmember', views.tripmember),

    # 주소창에 http://localhost/oraform/tripinsert 입력되면 views.py 파일 안의 tripinsert 메소드를 읽어라.
    # tripmember.html 에서 '가입하기' 버튼이 눌려지면 tripinsert 이 action 됨
    path('tripinsert', views.tripinsert),
    path('tripmemberlist', views.tripmemberlist),
    path('idchk', views.idchk),
]
