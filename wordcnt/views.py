from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from collections import Counter
import matplotlib.pyplot as plt

from wordcloud import wordcloud, WordCloud


def wordcntForm(request):
    return render(request, "wordcnt/wordcntForm.html")


# 1. Post,
@csrf_exempt
def wordcntProcess(request):
    wordv = request.POST['wordv']
    wordv = wordv.replace('\r\n', ' ')
    wordv = wordv.split(' ')
    print(wordv)
    print('=' * 30)
    wordv_cnt = Counter(wordv)
    print(wordv_cnt.most_common(50))
    STOPWORDS = ['', '할', '합니다.', '잘', '될', '것입니다.', '수', '합시다.']
    wordv_total = []

    for tag in wordv:
        if tag not in STOPWORDS:
            wordv_total.append(tag)
    print('=' * 30)
    wordv_cnt_total = Counter(wordv_total)
    print(wordv_cnt_total.most_common(20))
    wordv_cnt_totalList = wordv_cnt_total.most_common(20)
    return render(request, "wordcnt/wordcntProcess.html", {"wordv_cnt_totalList": wordv_cnt_totalList})


# -----------------------------------------------------------------------------------------------------

# 2 위의 함수를 복사해서 편집한
@csrf_exempt
def wordcntProcessVisual(request):
    wordv = request.POST['wordv']
    wordv = wordv.replace('\r\n', ' ')
    # 공백을 기준으로 출력한다.
    wordv = wordv.split(' ')
    print(wordv)
    print('=' * 30)
    wordv_cnt = Counter(wordv)

    print(wordv_cnt.most_common(50))
    STOPWORDS = ['', '할', '합니다.', '잘', '될', '것입니다.', '수', '합시다.']
    wordv_total = []
    for tag in wordv:
        if tag not in STOPWORDS:
            wordv_total.append(tag)

    print('=' * 30)
    wordv_cnt_total = Counter(wordv_total)
    print(wordv_cnt_total.most_common(20))
    wordv_cnt_totalList = wordv_cnt_total.most_common(20)

    # 한글 설정 경로
    font_location = '/usr/share/fonts/truetype/nanum/NanumGothicCoding.ttf'

    # 0에 가까울 수록 빈도의 순위, 1에 가까울 수록 빈도수에 더 큰 영향
    wordcloudv = WordCloud(font_path=font_location, background_color='white', max_words=50, relative_scaling=0.3,
                           width=800, height=450) \
        .generate_from_frequencies(wordv_cnt_total)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloudv)
    # 축 없애기
    plt.axis('off')
    plt.savefig('/home/kosmo1/PycharmProjects/myweb/wordcnt/static/assets/img/wordcnt.png')

    return render(request, "wordcnt/wordcntProcessVisual.html", {"wordv_cnt_totalList": wordv_cnt_totalList})
