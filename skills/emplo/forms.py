from .models import Employee, Employee1, SearchString
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, CharField, Form

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
class SearchStringForm(ModelForm):
    class Meta:
        model = SearchString
        fields = ['seastr']
        seastr = CharField(widget=Textarea)

class EmployeeForm1(ModelForm):
    class Meta:
        model = Employee1
        fields = ['name', 'position', 'level', 'skill']
        name = CharField(label='Имя', max_length=5, initial='Имя')
        position = CharField(label='Должность', initial='Должность')
        level = CharField(label='Уровень', initial='0')
        skill = CharField(label='Навыки', widget=Textarea, initial='Навыки через запятую', help_text='Введите навыки, разделенные запятыми')

        # widgets = {
        #     "name": TextInput(attrs= {
        #         'class':'form-control',
        #     }),
        #     "position": TextInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     "level": TextInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     "skill": TextInput(attrs={
        #         'class': 'form-control',
        #     }),
        # }
# class SearchStringForm(ModelForm):
#     class Meta:
#         model = SearchString
#         seastr = CharField()

class SearchForm(ModelForm):
    class Meta:
        model = SearchString
        fields = ['seastr']
        #seastr = CharField(label='Search', max_length=100)

from django import forms
from django.core import validators
from .models import Good

def check_for_positive(value):
    if value < 0:
        raise forms.ValidationError('NEEDS TO BE GREATER THEAN 0!')

class DoubleCheck(forms.ModelForm):
    # Form Fields go here
    class Meta:
        model = SearchString #Good
        exclude = ['name'] # Exclude name