from django.db import models


class Events(models.Model):
    event_name = models.CharField('Назва події', max_length=20)
    event_description = models.TextField('Опис події')
    event_date = models.DateTimeField('Час проведення події')

    def __str__(self):
        return self.event_name
