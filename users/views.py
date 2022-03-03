from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from users.forms import UserLoginForm


class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {"form": form}

        return render(request, 'users/login.html', context=context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)

                return HttpResponseRedirect(reverse('index'))

        return HttpResponseRedirect(reverse('users:login'))


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        pass
