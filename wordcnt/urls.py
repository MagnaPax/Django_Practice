from django.contrib import admin
from django.urls import path
from wordcnt import views

urlpatterns = [
    # 주소창에 http://localhost/wordcnt/wordcntForm 입력되면 views 파일 안의 wordcntForm 메소드를 읽어라.
    # home 메소드 안에는 wordcntForm.html 을 읽으라고 되어있음
    # http://localhost/wordcnt/wordcntForm ==> views.wordcntForm() ==> templates/wordcnt/wordcntForm.html
    path('wordcntForm', views.wordcntForm),

    path('wordcntProcess', views.wordcntProcess),

    path('wordcntProcessVisual', views.wordcntProcessVisual),
]
