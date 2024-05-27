from django.db import models

from core import consts


class Department(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def __str__(self) -> str:
        return self.name


class Worker(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, db_index=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255, blank=True)
    gender = models.IntegerField(verbose_name='Пол', choices=consts.GENDER_CHOICE)
    department = models.ForeignKey(Department, on_delete=models.PROTECT,
                                   verbose_name='Отделение', related_name='workers')

    dc = models.DateTimeField('Дата создания', auto_now_add=True)
    dm = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
