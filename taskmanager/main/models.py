from django.db import models
import datetime


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'


class Sign(models.Model):
    username = models.CharField('Имя пользователя', max_length=50)
    email = models.CharField('Почта', max_length=50)
    pass_1 = models.CharField('Описание', max_length=50)
    pass_2 = models.CharField('Описание', max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователя'


class Enter(models.Model):
    objects = None
    username = models.CharField('Имя пользователя', max_length=50)

    def __str__(self):
        return self.username


class Create(models.Model):
    LANG_CH = (
        ('d', 'Select language'),
        ('JS', 'JavaScript'),
        ('J', 'Java'),
        ('CP', 'C++'),
        ('CSh', 'C#'),
        ('C', 'C'),
        ('P', 'Python'),
        ('K', 'Kotlin'),
        ('H', 'HTML'),
        ('CSS', 'CSS'),
    )
    #username = models.CharField('Пользователь', max_length=50)
    filename = models.CharField('Название файла', max_length=50)
    code = models.TextField('Код')
    lang = models.CharField('Язык', max_length=20, choices=LANG_CH, default='Select language')
    date = models.DateField('Дата создания', default=datetime.datetime.now().strftime("%d.%m.%y"))

    def __str__(self):
        return self.filename

    class Meta:
        verbose_name = 'Сниппет'
        verbose_name_plural = 'Сниппеты'
