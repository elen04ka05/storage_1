from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Task, Sign
from .forms import EmailForm, Sign_in_Form


def welcome(request):
    return render(request, 'main/welcome.html')  # в кавычки вставляем html шаблон
    # return render(request, 'main/welcome.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def sign_in(request):
    if request.method == 'POST':
        form = Sign_in_Form(request.POST)
        if form.is_valid():
            user = Sign.objects.filter(username=form.cleaned_data['username'])
            if user:
                return redirect('home_page.html')
            else:
                error = 'Пользователя нет'
        else:
            error = 'Введенные данные неверны'
    form = Sign_in_Form()
    context = {
        'form': form
    }
    return render(request, 'main/sign_in.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['pass_1'] == form.cleaned_data['pass_2']:
                form.save()
                return redirect('sign_in.html')
            else:
                error = 'Повторение пароля неверно'

        else:
            error = 'Введенные данные неверны'

    form = EmailForm()
    context = {
        'form': form
    }
    return render(request, 'main/sign_up.html', context)


def home_page(request):
    return render(request, 'main/home_page.html')
