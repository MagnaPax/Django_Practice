from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from oraform.models import memberinsert, getMemberData, getIdchkData


def index(request):
    # templates/oraform/index.html 로 이동해라.
    return render(request, "oraform/index.html")


def tripmember(request):
    # templates/oraform/tripmember.html 로 이동해라.
    return render(request, "oraform/tripmember.html")


# 회원가입
@csrf_protect
def tripinsert(request):
    addr = (request.POST['id'], request.POST['pwd'],
            request.POST['name'], request.POST['email'],
            request.POST['tel'], request.POST['addr'])
    print('ID', addr)
    memberinsert(addr)
    return render(request, 'oraform/index.html')


# 회원리스트
def tripmemberlist(request):
    memlist = getMemberData()
    print(type(memlist))
    return render(request, 'oraform/memberlist.html', {'memlist': memlist})


def idchk(request):
    idv = request.GET["id"]
    # print("idv :", idv)
    idcnt = getIdchkData(idv)
    # print("함수 거친뒤 결과값: ", idcnt)
    if 0 in idcnt:
        msg = '사용 가능한 아이디 입니다'
        col = "blue"
    else:
        msg = '이미 사용중인 아이디 입니다'
        col = "red"
    return render(request, 'oraform/idchk.html', {'msg': msg, 'col':col})
