from django.db import models


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
    username = models.CharField('Имя пользователя', max_length=50)

    def __str__(self):
        return self.username
