from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from oraform.models import memberinsert


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
