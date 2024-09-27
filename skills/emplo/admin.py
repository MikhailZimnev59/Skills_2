from django.contrib import admin

from .models import Employee, SearchString

# Register your models here.
admin.site.register(Employee)
admin.site.register(SearchString)