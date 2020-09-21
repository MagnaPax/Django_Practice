from django.contrib import admin
from django.urls import path

from oraform import views

urlpatterns = [
    # 주소창에 http://localhost/oraform/main 입력되면 views.py 파일 안의 index 메소드를 읽어라.
    # http://localhost/oraform/main ==> views.index() ==> index.html
    path('main', views.index, name='main'),

    # 주소창에 http://localhost/oraform/tripmember 입력되면 views.py 파일 안의 tripmember 메소드를 읽어라.
    # index.html 에서 '회원가입'을 누르면 tripmember 실행
    path('tripmember', views.tripmember),

    # 주소창에 http://localhost/oraform/tripinsert 입력되면 views.py 파일 안의 tripinsert 메소드를 읽어라.
    # tripmember.html 에서 '가입하기' 버튼이 눌려지면 tripinsert 이 action 됨
    path('tripinsert', views.tripinsert),

    # index.html 에서 '회원리스트' 버튼이 눌려지면 tripmemberlist 실행
    path('tripmemberlist', views.tripmemberlist),

    # tripmember.html 에서 '중복확인' 버튼이 눌리 js 통해 처리됨
    # ajax를 이용하면 비동기식으로 브라우저 이동이 없음.
    path('idchk', views.idchk),
]
