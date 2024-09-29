from rest_framework import serializers
from .models import Employee, SearchString, Employee1

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'skill', 'level', 'fit_level']

class SearchString(serializers.ModelSerializer):
    class Meta:
        model = SearchString
        fields = ['seastr']

class EmployeeSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Employee1
        fields = ['id', 'name', 'position', 'skill', 'level', 'fit_level']