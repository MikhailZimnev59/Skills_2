path('search/', views.search, name='search'),
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

# class EmploUpdateView(UpdateView):
#     model = Employee1
#     template_name = 'emplo/edit_product_ggg.html'
#     form_class = EmployeeForm

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

#def ss(request, pk):
    # for s in SearchString.objects.all():
    #     print(s.id, s.seastr)
    # return HttpResponse('sssss')