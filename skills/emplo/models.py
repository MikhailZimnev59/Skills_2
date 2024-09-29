from django.db import models

class Employee(models.Model):
    name = models.CharField('Имя', max_length=5, default='')
    position = models.CharField('Должность', max_length=5, default='')
    skill = models.TextField('Навыки', default = '')
    level = models.CharField('Уровень', max_length = 5, default='')
    fit_level = models.FloatField('Соответствие', default=0)

    class Meta:
        verbose_name="Сотрудник"
        verbose_name_plural = 'Сотрудники'

    def get_absolute_url(self):
        return f"/emplo/{self.id}"

    def __str__(self):
        return f"{self.name}:{self.position}"

class Employee1(models.Model):
    name = models.CharField(max_length=5, default='')
    position = models.CharField(max_length=5, default='')
    skill = models.TextField(default = '')
    level = models.CharField(max_length = 5, default='')
    fit_level = models.FloatField(default=0)

    # class Meta:
    #     verbose_name="Сотрудник"
    #     verbose_name_plural = 'Сотрудники'

    def get_absolute_url(self):
        return f"/emplo/{self.id}"

    def __str__(self):
        return f"{self.name}:{self.position}"

class SearchString(models.Model):
    seastr = models.TextField('Поиск', default='')
    class Meta:
        verbose_name = "Поиск"
        verbose_name_plural = 'Поиск'

    def __str__(self):
        return self.seastr