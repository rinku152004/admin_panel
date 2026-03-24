from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User



def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


@login_required(login_url='/accounts/login/')
def create_admin(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        role_type = request.POST.get("role_type")

        user = User.objects.create_user(
            username=username,
            password=password,
            role_type=role_type
        )

        user.parent_admin = request.user
        user.level = request.user.level + 1
        user.save()

        messages.success(request, "Admin created successfully")

        return redirect("/dashboard/admin-tree/")

    return render(request, "accounts/create_admin.html")