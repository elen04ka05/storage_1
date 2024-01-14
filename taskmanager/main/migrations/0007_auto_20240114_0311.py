# Generated by Django 3.2.23 on 2024-01-14 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='a', max_length=50, verbose_name='Имя пользователя')),
            ],
        ),
        migrations.AddField(
            model_name='sign',
            name='pic',
            field=models.CharField(default='https://bronk.club/uploads/posts/2023-02/1677475753_bronk-club-p-milie-pikchi-otkritki-pinterest-15.jpg', max_length=50, verbose_name='Ссылка на фото'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='username',
            field=models.CharField(default='a', max_length=50, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Пользователь (хуесос)'),
        ),
    ]