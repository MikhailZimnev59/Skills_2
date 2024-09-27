from .models import Employee
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'level']
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

        }
# class ESForm(ModelForm):
#     class Meta:
#         model=ES
#         fields = ['emplo_id', 'skill_id', 'level']
#         widgets = {
#             # "emplo_id": I
#             "position": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Должность'
#             }),
#             "level": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Уровень'
#             }),
#
#         }