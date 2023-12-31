# Generated by Django 5.0 on 2023-12-25 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки сообщения')),
            ],
        ),
    ]
