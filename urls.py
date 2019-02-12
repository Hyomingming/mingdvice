from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #기본주소창인경우, views에 잇는 post_list 메소드 실행
]