from django.urls import path
from . import views


urlpatterns = [
    path('', views.emplo_home, name='emplo-home'),
    path('create/', views.create, name='create-emplo'),
    path('create/ggg/', views.create_ggg, name='create-emplo-ggg'),
    path('<int:pk>/', views.EmploDetailView.as_view(), name='emplo-detail'),
    path('<int:pk>/update/', views.EmploUpdateView.as_view(), name='emplo-update'),
    path('<int:pk>/delete/', views.EmploDeleteView.as_view(), name='emplo-delete'),
    path('mmm/', views.emplo_list_view, name='emplo-list'),
    path('ggg/', views.emplo_list_ggg, name='emplo-list-ggg'),
    path('ggg/edit/<int:pk>/', views.edit_emplo_ggg, name='edit-emplo-ggg'),
    # path('ggg/edit_es/<int:pk>/', views.edit_es, name='edit_es'),
    path('search/', views.search, name='search'),
#    path('ss/<int:pk>', views.ss, name = 'ss'),
    path('ss/<int:pk>', views.SearchStringUpdateView.as_view(), name='ss'),
]