from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def user_login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,
                      'account/login.html',
                      {
                          "form": login_form
                      })

    # request.method == 'POST'
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            user = authenticate(username=cleaned_data['username'],
                                password=cleaned_data['password'])
            if user:
                login(request, user)
                return HttpResponse('Wellcome You. You have been authenticated successfully')
            else:
                return HttpResponse('Sorry. Your username or password is not right.')
        else:
            return HttpResponse('Invalid login')
