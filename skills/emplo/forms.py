from .models import Employee, Employee1
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'level', 'skill']
        widgets = {
            "name": TextInput(attrs= {
                'class':'form-control',
                'placeholder':'Имя'
            }),
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            "level": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Уровень'
            }),
            "skill": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Навыки'
            }),


        }
class EmployeeForm1(ModelForm):
    class Meta:
        model = Employee1
        fields = ['name', 'position', 'level', 'skill']
        widgets = {
            "name": TextInput(attrs= {
                'class':'form-control',
            }),
            "position": TextInput(attrs={
                'class': 'form-control',
            }),
            "level": TextInput(attrs={
                'class': 'form-control',
            }),
            "skill": TextInput(attrs={
                'class': 'form-control',
            }),


        }
