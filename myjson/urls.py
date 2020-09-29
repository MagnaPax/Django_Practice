from django.urls import path

from myjson import views

urlpatterns = [

    # http://localhost:port/myjson/ ==> views.myjson()
    path('', views.myjson),

    # http://localhost:port/myjson/piedemo/ ==> views.pieChart() ==> piedemo1.html
    path('piedemo', views.pieChart),

    # http://localhost:port/myjson/jsondemo1/ ==> views.jsontest()
    path('jsondemo1',views.jsontest),

    # http://localhost:port/myjson/jsonview1/ ==> views.jsontestview() ==> jsonloadTest.html
    path('jsonview1',views.jsontestview),


    path('loadchart',views.loadchart),


    # 1) 브라우저 주소창에 /myjson/barchart 입력되면 barchart() 메소드 통해서 jsonloadTest.html 파일 갔다가
    # 2) 버튼 눌리면 아래 통해서 barchart_json() 메소드 갔다가
    # 3) 다시 이곳으로 돌아와서 barchart() 메소드 통해서 jsonloadTest.html 로 최종적으로 돌아감
    path('barchart',views.barchart),

    # 이건 /myjson/barchart 에서 버튼 눌렀을 때 json 데이터 받기 위한 barchart_json() 메소드로 보내는 것
    path('barchart_json', views.barchart_json),









]