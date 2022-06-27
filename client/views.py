from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from .forms import FriendForm
from .models import Friend


def indexView(request):
    form = FriendForm()
    friends = Friend.objects.all()
    return render(request, "index.html", {"form": form, "friends": friends})


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def postFriend(request):
    if is_ajax(request=request) and request.method == "POST":
        form = FriendForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize("json",[instance,],)
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def checkNickName(request):
    if is_ajax(request=request) and request.method == "GET":
        nick_name = request.GET.get("nick_name", None)
        if Friend.objects.filter(nick_name=nick_name).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)
