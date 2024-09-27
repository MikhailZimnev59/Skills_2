from .models import Employee
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'skill']
        widgets = {
            "name": TextInput(attrs= {
                'class':'form-control',
                'placeholder':'Имя'
            }),
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            "skill": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Навыки'
            }),


        }
