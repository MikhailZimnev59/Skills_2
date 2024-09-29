from django.contrib import admin

from .models import Employee, SearchString, Employee1

# Register your models here.
admin.site.register(Employee)
admin.site.register(SearchString)
admin.site.register(Employee1)