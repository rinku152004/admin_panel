from django.urls import path
from . import views

urlpatterns = [

    path('', views.roles_list, name="roles_list"),
    path('create_role/', views.create_role, name="create_role"),
]