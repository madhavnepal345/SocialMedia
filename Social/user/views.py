from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from.forms import LoginForm


def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)  #acccessing the login form
        if form.is_valid():
            data=form.cleaned_data
            user= authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return HttpResponse("user authhenticated and login")
            else:
                return HttpResponse("Invalid credintals")

             


    else:
        form= LoginForm()
        return render(request, 'login.html',{'form':form})
