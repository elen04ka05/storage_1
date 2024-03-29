from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Task, Sign, Enter
from .forms import EmailForm, Sign_in_Form, Sign_in_Email_Form, CreateForm


def welcome(request):
    return render(request, 'main/welcome.html')  # в кавычки вставляем html шаблон
    # return render(request, 'main/welcome.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def sign_in(request):
    if request.method == 'POST':
        form = Sign_in_Form(request.POST)
        if form.is_valid():
            user = Sign.objects.filter(username=form.cleaned_data['username'])
            if user:
                inp = Enter(1, user.values_list('username', flat=True).last())
                inp.save()
                return redirect('home_page.html')
            else:
                error = 'Пользователя нет'
        else:
            error = 'Введенные данные неверны'
    form = Sign_in_Form()
    # user_id = models.ForeignKey(MyUUIDModel, unique=True)
    # user_id = MyUUIDModel(models.Model)
    # print(user_id)
    context = {
        'form': form
    }
    return render(request, 'main/sign_in.html', context)


def snippet(request):
    return render(request, 'main/snippet.html')


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


def sign_in_email(request):
    if request.method == 'POST':
        form = Sign_in_Email_Form(request.POST)
        if form.is_valid():
            email = Sign.objects.filter(email=form.cleaned_data['email'])
            # username = Sign.objects.filter(email=form.cleaned_data['email'])
            if email:
                inp = Enter(1, email.values_list('username', flat=True).last())
                inp.save()
                return redirect('home_page.html')
            else:
                error = 'Пользователя нет'
        else:
            error = 'Введенные данные неверны'
    form = Sign_in_Email_Form()
    context = {
        'form': form
    }
    return render(request, 'main/sign_in_email.html', context)


def home_page(request):
    return render(request, 'main/home_page.html')


def profile(request):
    id = Enter.objects.latest('id')
    if id is None:
        username = "ZAEBALAS"
    else:
        username = id.username

    return render(request, 'main/profile.html', {'username': username})


def create(request):
    error = ''
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippet.html')
        else:
            error = 'Ошибка ввода'
    form = CreateForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


@csrf_exempt
def update_username(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_username = data.get('new_username')
        if new_username:
            try:
                user_input = Enter.objects.last()
                user = Sign.objects.filter(username=user_input.username)
                print(user)
                user_input.username = new_username
                user_input.save()
                user.username = new_username
                print(user.username)
                user.save()
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})
