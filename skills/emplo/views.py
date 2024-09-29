from django.shortcuts import render, redirect
from .models import Employee, SearchString, Employee1
from .forms import EmployeeForm, EmployeeForm1
from django.views.generic import DetailView, UpdateView, DeleteView
from .serializers import EmployeeSerializer


def emplo_list_ggg(request):
    products = Employee1.objects.all()

    if request.method == "POST":
        form = EmployeeForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emplo-list-ggg')  # Обновляем страницу

    context = {
        'products': products,
        'form': EmployeeForm1()
    }
    return render(request, 'emplo/emplo_list_ggg.html', context)

class EmploUpdateView(UpdateView): ###############
    model = Employee1
    template_name = 'emplo/edit_product_ggg.html'
    form_class = EmployeeForm

def edit_emplo_ggg(request, pk):
    emplo = Employee1.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm1(request.POST, instance=emplo)
        if form.is_valid():
            form.save()
            return redirect('emplo-list-ggg')
    else:
        form = EmployeeForm1(instance=emplo)
    context = {
            'form': form,
            'product': emplo
    }
    return render(request, 'emplo/edit_emplo_ggg.html', context)

def count_fit(emp_skill, skill_req):
    e = [i.strip() for i in emp_skill.split(',')]
    s = [i.strip() for i in skill_req.split(',')]
    return 0 if not s else round(sum(i in e for i in s) / len(s) * 100, 1)

def emplo_list_view(request):
    queryset = SearchString.objects.all()
    skill_req = 'No info' if not queryset else queryset[0].seastr
    queryset = Employee1.objects.all()
    for emp in queryset:
        emp.fit_level = count_fit(emp.skill, skill_req)
        emp.save()
    queryset = Employee1.objects.order_by('-fit_level')

    # Сериализуем данные
    serializer = EmployeeSerializer(queryset, many=True)

    # Передаем сериализованные данные в шаблон
    context = {
        'data': serializer.data
    }

    return render(request, 'emplo/emplo_list.html', context)
def emplo_home(request):
    emplo = Employee1.objects.order_by('name')
    return render(request, 'emplo/emplo_home.html', {'emplo':emplo})

class EmploDetailView(DetailView):
    model = Employee1
    template_name = 'emplo/details_view.html'
    context_object_name = 'article'

class EmploUpdateView(UpdateView):
    model = Employee1
    template_name = 'emplo/update.html'
    form_class = EmployeeForm1

class EmploDeleteView(DeleteView):
    model = Employee1
    success_url = '/emplo/'
    template_name = 'emplo/emplo_delete.html'

def create(request):
    error=''
    if request.method == 'POST':
        form = EmployeeForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emplo-home')
        else:
            error = 'Форма была неверной'

    form = EmployeeForm1()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'emplo/create_emplo.html', data)

# def edit_es(request, pk):
#     emplo = Employee.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EForm(request.POST, instance=emplo)
#         if form.is_valid():
#             form.save()
#             return redirect('emplo-list-ggg')
#     else:
#         form = EmployeeForm(instance=emplo)
#     context = {
#             'form': form,
#             'product': emplo
#     }
#     return render(request, 'emplo/edit_emplo_ggg.html', context)
