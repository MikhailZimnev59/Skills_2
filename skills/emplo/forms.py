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
        name = CharField(label='Имя', max_length=20, initial='Имя')
        position = CharField(label='Должность', max_length=20, initial='Должность')
        level = CharField(label='Уровень', max_length=5, initial='0')
        skill = CharField(label='Навыки',  max_length=50, initial='Навыки через запятую')


class SearchForm(ModelForm):
    class Meta:
        model = SearchString
        fields = ['seastr']
        #seastr = CharField(label='Search', max_length=100)

from django import forms

def check_for_positive(value):
    if value < 0:
        raise forms.ValidationError('NEEDS TO BE GREATER THEAN 0!')

class DoubleCheck(forms.ModelForm):
    # Form Fields go here
    class Meta:
        model = SearchString #Good
        exclude = ['name'] # Exclude name