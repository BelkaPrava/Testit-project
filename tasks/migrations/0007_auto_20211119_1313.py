# Generated by Django 3.2.6 on 2021-11-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20211112_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='answer',
            field=models.CharField(max_length=500, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='task',
            name='condition',
            field=models.TextField(verbose_name='Задание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
