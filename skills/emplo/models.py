from django.db import models

class Employee(models.Model):
    name = models.CharField('Имя', max_length=20, default='')
    position = models.CharField('Должность', max_length=20, default='')
    level = models.CharField('Уровень', max_length = 5, default='')

    class Meta:
        verbose_name="Сотрудник"
        verbose_name_plural = 'Сотрудники'

    def get_absolute_url(self):
        return f"/emplo/{self.id}"

    def __str__(self):
        return f"{self.name}:{self.level}"

# class ES(models.Model):
#     emplo_id = models.IntegerField()
#     skill_id = models.IntegerField()
#     level = models.CharField('Level', max_length=5, default='')
#
#     def __str__(self):
#         return f"{self.emplo_id}{self.skill_id}{self.level}"