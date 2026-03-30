from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('admin_list/', views.admin_list, name='admin_list'),
    path('admin_tree/', views.admin_tree, name='admin_tree'),
    path('reports/', views.reports, name='reports'),
    
]