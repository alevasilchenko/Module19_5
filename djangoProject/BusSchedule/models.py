from django.db import models


class BusRoute(models.Model):
    number = models.CharField(max_length=4)  # номер маршрута (с возможностью добавления символов алфавита)
    description = models.CharField(max_length=100)  # путь следования
    schedule = models.TextField()  # расписание

    def __str__(self):
        return f"{self.number}: {self.description}"
