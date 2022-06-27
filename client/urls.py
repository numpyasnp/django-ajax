from django.urls import path

from client.views import checkNickName, indexView, postFriend

urlpatterns = [
    path("", indexView),
    path("post/ajax/friend", postFriend, name="post_friend"),
    path("get/ajax/validate/nickname", checkNickName, name="validate_nickname"),
]
