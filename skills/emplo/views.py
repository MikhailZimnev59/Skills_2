from django.shortcuts import render, redirect, HttpResponse
from .models import Employee, SearchString, Employee1, Good
from .forms import EmployeeForm, EmployeeForm1, SearchForm, SearchStringForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .serializers import EmployeeSerializer



# from .forms import SearchForm
# # from .models import YourModel

from django.shortcuts import render
# from .models import Good
from . import forms

# Create your views here.
def search(request):
    print('search')
    #form = forms.DoubleCheck
    # if sso := SearchString.objects.all():
    #     query = sso[0].seastr
    # else:
    #     query = ''
    model = SearchString
    form = SearchStringForm   #SearchForm
    form_dict = {'form':form,
                'result':False,
                 # 'query': query,
                 }

    if request.method == 'POST':
        #form = forms.DoubleCheck(request.POST)
        form = SearchForm(request.POST)

        # if form.is_valid():
        #     print(f"{form=}")
        #     result = str(Employee1.objects.all())    #.filter(height = {ТО ЧТО ВВЁЛ ЮЗЕР}, width = {ТО ЧТО ВВЁЛ ЮЗЕР}, diameter = {ТО ЧТО ВВЁЛ ЮЗЕР}))
        #     form_dict['result'] = result
        if form.is_valid():
            print('VALIDATION SUCCESS!')
            ss = form.cleaned_data.get("seastr")
            print(f"{ss=}")
            # height_user = form.cleaned_data.get("height")
            # width_user = form.cleaned_data.get("width")
            # diameter_user = form.cleaned_data.get("diameter")
            result = str(Employee1.objects.all()) #.filter(height=height_user, width=width_user, diameter=diameter_user))
            form_dict['result'] = result
    return render(request, 'emplo/search1.html', context = form_dict)

# def search_view(request):
#     form = SearchForm()
#     results = []
#     print(f"{request.method=} and {request.GET=}")
#     if request.method == 'GET' and 'query' in request.GET:
#
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             print(f"{query=}")
#             results = Employee1.objects.filter(fit_level__gt=0)  # Adjust as needed
#     results = Employee1.objects.all()
#     return render(request, 'emplo/search.html', {'form': form, 'results': results})
def emplo_list_ggg(request):
    print('emplo_list_ggg')
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

# class EmploUpdateView(UpdateView):
#     model = Employee1
#     template_name = 'emplo/edit_product_ggg.html'
#     form_class = EmployeeForm

def edit_emplo_ggg(request, pk):
    print('edit_emplo_ggg')
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
    e = [i.strip().lower() for i in emp_skill.split(',')]
    s = [i.strip().lower() for i in skill_req.split(',')]
    return 0 if not s else round(sum(i in e for i in s) / len(s) * 100, 1)

def emplo_list_view(request):
    print('emplo_list_view')
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
def emplo_list_view_old(request):
    print('emplo_list_view')
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
    print('emplo_home')
    emplo = Employee1.objects.order_by('name')
    return render(request, 'emplo/emplo_home.html', {'emplo':emplo})

class EmploDetailView(DetailView):
    print('EmpoDetailView')
    model = Employee1
    template_name = 'emplo/details_view.html'
    context_object_name = 'article'

class EmploUpdateView(UpdateView):
    print('EmpoUpdateView')
    model = Employee1
    template_name = 'emplo/update.html'
    form_class = EmployeeForm1

class EmploDeleteView(DeleteView):
    print('EmpoDeleteView')
    model = Employee1
    success_url = '/emplo/'
    template_name = 'emplo/emplo_delete.html'

def create(request):
    print('create')
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
def create_ggg(request):
    print('create_ggg')
    error=''
    if request.method == 'POST':
        form = EmployeeForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emplo-list-ggg')
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

class SearchStringUpdateView(UpdateView):
    model = SearchString
    template_name = 'emplo/ss.html'
    form_class = SearchString

#def ss(request, pk):
    # for s in SearchString.objects.all():
    #     print(s.id, s.seastr)
    # return HttpResponse('sssss')
class SearchStringUpdateView(UpdateView):
    print('ss')
    model = SearchString
    template_name = 'emplo/ss.html'
    form_class = SearchStringForm