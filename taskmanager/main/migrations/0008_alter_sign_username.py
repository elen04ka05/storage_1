# Generated by Django 3.2.23 on 2024-01-14 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20240114_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Имя пользователя'),
        ),
    ]
