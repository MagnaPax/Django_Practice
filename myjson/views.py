from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render
import pandas as pd

from myjson.models import make_dfall, make_testJson


def pieChart(request):
    return render(request, "myjson/piedemo1.html")


def loadchart(request):
    return 1


def jsontest(request):
    return JsonResponse([['a','30','20','35','45','55','66','75'],
                        ['b','10', '20', '30', '40', '50', '60', '70']],
                        safe=False)

def jsontestview(request):
    return render(request,"myjson/jsonloadTest.html")



def myjson(request):
    df3 = make_dfall()
    # df3.to_json('/home/kosmo1/PycharmProjects/myweb/myjson/static/savedJson', orient='records', force_ascii=False) #json 파일 저장하기
    # print("test")
    # return render(request, 'myjson/json1.html')
    jsondata = df3.to_json(orient='records', force_ascii=False)
    print(jsondata)
    # return render(request, 'myjson/json1.html')
    return JsonResponse({'data1': jsondata}, json_dumps_params={'ensure_ascii': False})


def barchart_json(request):
    df3 = make_testJson()
    jsondata = df3.to_json(orient='records', force_ascii=False)
    print("가져온 json\n", jsondata)
    #return JsonResponse({'data1': jsondata}, json_dumps_params={'ensure_ascii': False})
    # return  JsonResponse(jsondata)

    return JsonResponse([['a','30','20','35','45','55','66','75'],
                         ['b','10', '20', '30', '40', '50', '60', '70'],
                         ['c', '10', '20', '30', '40', '50', '60', '70'],
                         ['d', '10', '20', '30', '40', '50', '60', '70']],
                         safe=False)

def barchart(request):
    return render(request, 'myjson/barChart.html')




