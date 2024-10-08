# Generated by Django 5.1.1 on 2024-09-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplo', '0002_employee_fit_level_employee_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seastr', models.TextField(default='', verbose_name='Поиск')),
            ],
            options={
                'verbose_name': 'Поиск',
                'verbose_name_plural': 'Поиск',
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='fit_level',
            field=models.FloatField(default=0, verbose_name='Соответствие'),
        ),
    ]
