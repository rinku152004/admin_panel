from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('admins/', views.admin_list, name='admin_list'),
    path('admin-tree/', views.admin_tree, name='admin_tree'),
    path('reports/', views.reports, name='reports'),
    
]