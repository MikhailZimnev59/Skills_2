from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .serializers import EmployeeSerializer

def edit_es(request, pk):
    emplo = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EForm(request.POST, instance=emplo)
        if form.is_valid():
            form.save()
            return redirect('emplo-list-ggg')
    else:
        form = EmployeeForm(instance=emplo)
    context = {
            'form': form,
            'product': emplo
    }
    return render(request, 'emplo/edit_emplo_ggg.html', context)


def emplo_list_ggg(request):
    products = Employee.objects.all()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emplo-list-ggg')  # Обновляем страницу

    context = {
        'products': products,
        'form': EmployeeForm()
    }
    return render(request, 'emplo/emplo_list_ggg.html', context)

class EmploUpdateView(UpdateView): ###############
    model = Employee
    template_name = 'emplo/edit_product_ggg.html'
    form_class = EmployeeForm

def edit_emplo_ggg(request, pk):
    emplo = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emplo)
        if form.is_valid():
            form.save()
            return redirect('emplo-list-ggg')
    else:
        form = EmployeeForm(instance=emplo)
    context = {
            'form': form,
            'product': emplo
    }
    return render(request, 'emplo/edit_emplo_ggg.html', context)

def emplo_list_view(request):
    # Получаем все объекты из базы данных
    queryset = Employee.objects.all()

    # Сериализуем данные
    serializer = EmployeeSerializer(queryset, many=True)

    # Передаем сериализованные данные в шаблон
    context = {
        'data': serializer.data
    }

    return render(request, 'emplo/emplo_list.html', context)
def emplo_home(request):
    emplo = Employee.objects.order_by('name')
    return render(request, 'emplo/emplo_home.html', {'emplo':emplo})

class EmploDetailView(DetailView):
    model = Employee
    template_name = 'emplo/details_view.html'
    context_object_name = 'article'

class EmploUpdateView(UpdateView):
    model = Employee
    template_name = 'emplo/create.html'
    form_class = EmployeeForm

class EmploDeleteView(DeleteView):
    model = Employee
    success_url = '/emplo/'
    template_name = 'emplo/emplo_delete.html'

def create(request):
    error=''
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emplo-home')
        else:
            error = 'Форма была неверной'

    form = EmployeeForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'emplo/create_emplo.html', data)
