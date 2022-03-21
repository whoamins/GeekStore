from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from users.forms import UserLoginForm, UserRegistrationForm, EditForm


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

                return HttpResponseRedirect(reverse('products:index'))

        # return HttpResponseRedirect(reverse('users:login'))
        return render(request, 'users/login.html', context={'form': form})


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {"form": form}

        return render(request, 'users/register.html', context=context)

    def post(self, request):
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, message='You have been successfully registered')

            return HttpResponseRedirect(reverse('users:login'))

        # return HttpResponseRedirect(reverse('users:register'))
        return render(request, 'users/register.html', context={'form': form})


class ProfileView(View):
    def get(self, request):
        form = EditForm(instance=request.user)
        context = {"form": form}

        return render(request, 'users/profile.html', context=context)

    def post(self, request):
        form = EditForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

        return HttpResponseRedirect(reverse('products:index'))
