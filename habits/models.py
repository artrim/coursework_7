from datetime import timedelta

from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель привычки',
                              **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='место выполнения привычки')
    time = models.DateTimeField(verbose_name='время выполнения привычки')
    action = models.TextField(verbose_name='действие, которое представляет собой привычка')
    pleasant_habit_sign = models.BooleanField(verbose_name='признак приятной привычки', default=False)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.PositiveSmallIntegerField(verbose_name='переодичность', default=1)
    award = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    duration = models.DurationField(verbose_name='продолжительность', default=timedelta(seconds=120))
    is_published = models.BooleanField(default=True, verbose_name='признак публичности')

    def __str__(self):
        return f'{self.owner} делает {self.action}, {self.periodicity} раз в неделю'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
