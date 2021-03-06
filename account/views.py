from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm, RegistrationForm, UserProfileForm


def register(request):
    if request.method != 'POST':
        user_form = RegistrationForm()
        user_profile_form = UserProfileForm()
        return render(request,
                      'account/register.html',
                      {
                          "form": user_form,
                          "profile": user_profile_form,
                      })
    else:
        user_form = RegistrationForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            new_profile = user_profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            return HttpResponse('Successfully')
        else:
            return HttpResponse('Sorry, your can not register.')

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
