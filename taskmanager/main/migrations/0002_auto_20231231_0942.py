# Generated by Django 3.2.23 on 2023-12-31 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
                ('pass_1', models.CharField(max_length=50, verbose_name='Описание')),
            ],
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'задача', 'verbose_name_plural': 'задачи'},
        ),
    ]
