from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from login.models import getLoginChk


def main(request):
    return render(request, 'login/index.html')


@csrf_protect
def loginform(request):
    # login 이 되어서 이미 세션이 존재한다면 메인페이지로 이동한다
    if 'user_id' in request.session:
        return redirect("/login")
    if request.method == 'POST':
        user_id = request.POST['id']
        user_pwd = request.POST['pwd']
        print('user_id:', user_id)
        print('user_pwd:', user_pwd)

        # db_id = 'xman'
        # db_pwd = '11'
        # db_name = '김길동'
        #
        # if user_id in db_id and user_pwd in db_pwd:
        #     print("login complete!")
        #     request.session['user_id'] = db_id
        #     request.session['user_name'] = db_name
        #     return redirect("/login")
        # else:
        #     print("login 실패")
        #     msg = '아이디나 비밀번호가 잘못 되었습니다'
        #     return render(request, "login/login.html", {"error": msg})

        res = getLoginChk(id=user_id, pwd=user_pwd)
        print('=' * 30)
        print(res)
        if len(res) > 0:
            print('로그인 성공')
            request.session['user_id'] = user_id
            request.session['user_name'] = res[0][1]
        else:
            print('로그인 실패')
            msg = '아이디나 비밀번호가 잘못 되었습니다'
            return render(request, "login/login.html", {"error": msg})
        return redirect("/login")
    return render(request, "login/login.html")


# logout
def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect("/login")
