# Create your models here. Эта модель содержит поля для имени, email, сообщения и даты отправки.
from django.db import models

class Feedback(models.Model):
    name = models.CharField('ФИО', max_length=100)
    email = models.EmailField('E-mail')
    message = models.TextField('Сообщение')
    date_sent = models.DateTimeField('Дата отправки сообщения', auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date_sent}"


# Модель для собак, котов

class Pet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name