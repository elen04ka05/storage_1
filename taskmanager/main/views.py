from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Sign, Create, Input
from .forms import EmailForm, Sign_in_Form, CreateForm, Sign_in_Email_Form


def welcome(request):
    return render(request, 'main/welcome.html')  # в кавычки вставляем html шаблон
    # return render(request, 'main/welcome.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def sign_in(request):
    if request.method == 'POST':
        form = Sign_in_Form(request.POST)
        if form.is_valid():
            user = Sign.objects.filter(username=form.cleaned_data['username'])
            if user:
                inp = Input(1, user.values_list('username', flat=True).last())
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

    id = Input.objects.latest('id')
    print(id)

    return render(request, 'main/profile.html', {'username': id})


def snippet(request):
    return render(request, 'main/snippet.html')


def history(request):
    return render(request, 'main/history.html')


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