from pydoc import cli
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from . import users_client
# Web-View for GRPC-Client

client = users_client.UserClient()

@csrf_exempt
def indexView(request):
    return render(request, 'index.html')


@csrf_exempt
def loginView(request):
    return render(request, 'login.html')


@csrf_exempt
def loginCheck(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    result = client.getLogin(username=username, password=password)
    messages.success(request, result)
    return redirect('/index')

@csrf_exempt
def regView(request):
    return render(request, 'reg.html')

@csrf_exempt
def regDo(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    result = client.getRegister(username=username, password=password)
    messages.success(request, result)
    return redirect('/index')

@csrf_exempt
def deleteView(request):
    return render(request, 'delete.html')


@csrf_exempt
def deleteDo(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    result = client.getDelete(username=username, password=password)
    messages.success(request, result)
    return redirect('/index')


@csrf_exempt
def updateView(request):
    return render(request, 'update.html')

@csrf_exempt
def updateDo(request):
    old_username = request.POST.get('old_username')
    old_password = request.POST.get('old_password')
    new_username = request.POST.get('new_username')
    new_password = request.POST.get('new_password')
    result = client.getUpdate(
        old_username=old_username,
        old_password=old_password,
        new_username=new_username,
        new_password=new_password
    )
    messages.success(request, result)
    return redirect('/index')



