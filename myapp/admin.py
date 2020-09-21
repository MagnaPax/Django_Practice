from django.contrib import admin

from myapp.models import Post
# 관리자 화면에 출력할 필드 목록을 정의한다.
# 이때 번호는 자동증가를 설정했기 때문에 할 필요가 없다.

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'author')

# 관리자 기능에 추가할 모델을 등록
admin.site.register(Post, PostAdmin)