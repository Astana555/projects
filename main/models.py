#бд еще делаю
# Create your models here. Эта модель содержит поля для имени, email, сообщения и даты отправки.

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date_sent}"