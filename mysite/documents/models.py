from django.db import models


class Groups(models.Model):
    group_name = models.CharField('Група документу', max_length=20)

    def __str__(self):
        return self.group_name


class Documentations(models.Model):
    category = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='Documentations')
    title = models.TextField('Назва документу')
    content = models.TextField('Документ')
    upload_date = models.DateField('Дата публікації', auto_now_add=True)
    update_date = models.DateField('Дата оновлення', auto_now=True)
    is_published = models.BooleanField('Публікація', default=True)

    def __str__(self):
        return self.title
