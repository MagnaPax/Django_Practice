from django.urls import path
from shop import views

urlpatterns=[
    # http://localhost/shop/shoplist ==> views.py 의 product_list()호출
    path('shoplist', views.product_list),

    # http://localhost/shop/product_write ==> views.py 의 product_write()호출
    path('product_write', views.product_write),

    path('product_insert', views.product_insert),
    path('product_detail', views.product_detail),
    #path('product_update', views.product_upform),
    #path('product_update', views.product_update),
]
