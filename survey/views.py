from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from survey.models import Survey, Answer


def home(request):
    # Survey.objects : 모든 레코드를 의미, filter 조건(where 절에 해당) 즉 status 가 y 인 모든 레코드
    # order_by 필드명 앞에 -는 내림차순을 의미한다.
    # [0] 레코드중 첫번째 요소 [0번째 인덱스]
    survey = Survey.objects.filter(status="y").order_by("-survey_idx")[0]

    # templates/survey/list.html 로 이동해라. 위 조건에 해당되는 레코드와 함께
    return render(request, "survey/list.html", {"survey": survey})


@csrf_protect
def save_survey(request):
    # 문제 번호와 응답번호를 Answer 객체에 저장한다.
    survey_idx = request.POST["survey_idx"]
    print("타입: ", type(survey_idx))
    dto = Answer(survey_idx=int(request.POST["survey_idx"]), num=request.POST["num"])
    # insert query 가 호출이 됨(db에 저장됨)
    dto.save()
    # success.html로 이동한다
    return render(request, "survey/success.html")


def show_result(request):
    # 문제 번호
    idx = request.GET["survey_idx"]
    # select * from survey where survey_idx=1 과 같다
    ans = Survey.objects.get(survey_idx=idx)
    # 각 문장에 대한 값으로 리스트를 만들어 놓는다
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4]
    # Survey.objects.raw(""" SQL문 """, param)
    surveyList = Survey.objects.raw("""
    select survey_idx, num, count(num) sum_num from survey_answer where survey_idx=%s
    group by survey_idx, num order by num
    """, idx)
    print(surveyList)
    # 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
    '''
    list(zip([1,2,3], [4,5,6]))
    ==> [(1,4), (2,5), (3,6)]
    '''
    surveyList = zip(surveyList, answer)
    print(surveyList)
    return render(request, "survey/result.html", {'surveyList': surveyList})
