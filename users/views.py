from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import *
from .forms import *


# Index Page
def index(request):
    return render(request, 'main.html')


def registerUser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            userMessage = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + userMessage)

            # don't need to create the empty object. We will set route to create/update/delete objects later on
            #StockInfo.objects.create(
            #    user=user,
            #)

            return redirect('users:loginuser')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'registration/registerUser.html', context)

#Login User
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username') # we get this from the form (loginuser.html) input name=""
        password = request.POST.get('password') # we get this from the form (loginuser.html) input password=""

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:index')
        else:
            messages.info(request, 'Username OR password is incorrect') # flash a message

    context = {}
    return render(request, 'accounts/loginuser.html', context)

# Logout User Page (no template needed)
def logoutUser(request):
    logout(request)
    return redirect('users:loginuser')

# Report Page
@login_required(login_url='users:loginuser')
def report(request):
    stock_info = StockInfo.objects.all()

    totalStockInfo = stock_info.count()

    context = {
        'stock_info': stock_info,
        'totalStockInfo': totalStockInfo
    }

    return render(request, 'accounts/report.html', context)

# add  stocks information in database
@login_required(login_url='users:loginuser')
def addInfo(request):
  form = StockInfoForm()
  if request.method == 'POST':
    form = StockInfoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('users:report')
  context = {"form": form}
  return render(request, "users/addinfoform.html", context)

# delete stocks information from database
@login_required(login_url='users:loginuser')
def deleteInfo(request, pk):
  StockInfoToDelete = StockInfo.objects.get(id=pk)
  if request.method == "POST":
    StockInfoToDelete.delete()
    return redirect('users:report')
  context = {"item": StockInfoToDelete}
  return render(request, "users/deleteinfoform.html", context)


# update stock info
@login_required(login_url='users:loginuser')
def updateInfo(request, pk):
    StockInfoToUpdate = get_object_or_404(StockInfo, pk=pk)
    form = StockInfoToUpdateForm(instance=StockInfoToUpdate)
    if request.method == 'POST':
        form = StockInfoToUpdateForm(request.POST, instance=StockInfoToUpdate)
        if form.is_valid():
            form.save()
            return redirect('users:report')
    context = {"form": form}
    return render(request, "users/updateinfoform.html", context)
