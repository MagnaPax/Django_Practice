from django.shortcuts import render
from myapp.models import Post


def home(request):
    # .order_by('idx') : 오름차순
    # .order_by('-idx') : 내림차순
    # select * from address_address order by name asc or desc
    items = Post.objects.order_by('idx')

    # count value
    # Post 테이블의 레코드 갯수를 저장
    # select count(*) from address_address
    post_count = Post.objects.all().count()
    return render(request, "myapp/index.html", {'items': items, 'post_count': post_count})



    #
    # # .order_by('name') : 오름차순
    # # .order_by('-name') : 내림차순
    # # select * from address_address order by name asc or desc
    # items = Address.objects.order_by('name')
    #
    # # count value
    # # address 테이블의 레코드 갯수를 저장
    # # select count(*) from address_address
    # address_count = Address.objects.all().count()
    # return render(request, "address/list.html", {'items': items, 'address_count': address_count})