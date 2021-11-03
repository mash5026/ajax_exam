from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TestAjax
from .forms import Regi
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.

def index(request):
    my_test = TestAjax.objects.all()
    if request.is_ajax():
        my_form = Regi(request.POST)
        if my_form.is_valid():
            my_form.save()
            return JsonResponse({"msg":"success"})
        else:
            return JsonResponse({"msg":"error"})
    else:
        my_form = Regi()
    return render(request, "ajax_app/first.html", {'form':my_form, "my_test":my_test})


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this username already exists."
    return JsonResponse(data)




