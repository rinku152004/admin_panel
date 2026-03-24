from django.shortcuts import render, redirect
from .models import Role
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def roles_list(request):

    roles = Role.objects.all()

    return render(request, "roles/roles.html", {"roles": roles})

def create_role(request):

    if request.method == "POST":
        name = request.POST.get("name")

        Role.objects.create(name=name)

        return redirect("/roles/")

    return render(request, "roles/create_role.html")