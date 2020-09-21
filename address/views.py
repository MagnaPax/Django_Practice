from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from address.models import Address


def home(request):
    # .order_by('name') : 오름차순
    # .order_by('-name') : 내림차순
    # select * from address_address order by name asc or desc
    items = Address.objects.order_by('name')

    # count value
    # address 테이블의 레코드 갯수를 저장
    # select count(*) from address_address
    address_count = Address.objects.all().count()
    return render(request, "address/list.html", {'items': items, 'address_count': address_count})
    # return render(request, "index.html")


def write(request):
    # address/templates/address/write.html 페이지로 이동
    return render(request, "address/write.html")


# 크로스 사이트 스크립팅 공격을 방지하기 위한 코드
# @requires_csrf_token : default
# csrf_protect : 반드시 csrf를.. 검증하기
# @csrf_exempt : 해제
@csrf_protect
def insert(request):
    # POST 방식으로 전달된 파라미터값
    # name = request.POST['name']
    # tel = request.POST['tel']
    # email = request.POST['email']
    # address = request.POST['address']
    #
    # print('name: ', name)
    # print('tel: ', tel)
    # print('email: ', email)
    # print('address: ', address)

    addr = Address(name=request.POST['name'],
                   tel=request.POST['tel'],
                   email=request.POST['email'],
                   address=request.POST['address'])
    # DB에 insert 처리
    addr.save()
    return redirect('/address/write')
    # return redirect('/address/hahaha')


def detail(request):
    idv = request.GET['idx']
    # select # from address_address where idx= idv
    addr = Address.objects.get(idx=idv)
    return render(request, 'address/detail.html', {'addr': addr})


@csrf_protect
def delete(request):
    # 삭제할 주소록 번
    id = request.POST['idx']
    print('번호: ', id)
    # 선택한 레코드가 삭제됨 - Address.objects 전체 레코드에서
    Address.objects.get(idx=id).delete()
    # 수정 후 리다이렉트로 목록으로 이동
    return redirect('/address/')


def update(request):
    id = request.POST['idx']
    name = request.POST['name']
    email = request.POST['email']
    address = request.POST['address']
    print('id number: ', id, '\nname: ', name, '\nemail: ', email, '\naddress: ', address)

    # 수정할 내용을 편집
    addr = Address(idx=id,
                   name=request.POST['name'],
                   tel=request.POST['tel'],
                   email=request.POST['email'],
                   address=request.POST['address'])
    # 레코드가 수정됨
    addr.save()
    # 수정 후 리다이렉트로 목록으로 이동
    return redirect('/address/')
