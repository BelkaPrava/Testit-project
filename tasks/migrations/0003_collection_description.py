# Generated by Django 3.2.6 on 2021-10-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(default='Описание коллекции', max_length=512),
        ),
    ]
