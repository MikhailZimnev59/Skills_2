# Generated by Django 5.1.1 on 2024-09-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplo', '0005_employee1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee1',
            name='fit_level',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='level',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='name',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='position',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='skill',
            field=models.TextField(default=''),
        ),
    ]
