from django.shortcuts import render


# Default index

def home(request):
    msg = '안녕하세요'
    name = '홍길동'
    age = 30
    return render(request, "index.html", {'name': name, 'msg': msg, 'age': age})


def profile(request):
    msg = '내 프로필'
    name = '한천희'
    unit = 'Kosmo'
    skills = 'Python'

    return render(request, 'profile.html', {'msg': msg, 'name': name, 'unit': unit, 'skills': skills})


# get 방식 처리하기
def getdemo(request):
    # request.GET['param']
    num = request.GET['num']
    print('num:', num)
    # num을 int형으로 타입캐스팅
    num = int(num)
    range1 = [x for x in range(0, 10)]
    return render(request, "getdemo.html", {'num': num, 'range': range1})
