from django.contrib import admin

# Register your models here.
#
from address.models import Address
# 관리자 화면에 출력할 필드 목록을 정의한다.
# 이때 번호는 자동증가를 설정했기 때문에 할 필요가 없다.

class AddressAdmin(admin.ModelAdmin):

    list_display = ('name', 'tel', 'email', 'address')
# 관리자 기능에 추가할 모델을 등록
admin.site.register(Address, AddressAdmin)
