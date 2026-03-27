from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()

# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists")
#             return redirect("/accounts/register/")

#         user = User.objects.create_user(
#             username=username,
#             password=password
#         )

#         messages.success(request, "Account created successfully")
#         return redirect("/accounts/login/")

#     return render(request, "accounts/register.html")

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

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("/accounts/create-admin/")

        user = User.objects.create_user(
            username=username,
            password=password,
            role_type=role_type
        )

        # Set parent admin and level
        user.parent_admin = request.user
        user.level = request.user.level + 1
        user.save()

        messages.success(request, f"{user.role_type} created successfully")

        return redirect("/accounts/create-admin/")

    return render(request, "accounts/create_admin.html")

@login_required(login_url='/accounts/login/')
def logout_view(request):
    logout(request)
    messages.info(request, 'Logout successfully')
    return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def delete_admin(request, id):

    user = get_object_or_404(User, id=id)

    # Security check: Only parent admin or super admin can delete
    if request.user == user.parent_admin or request.user.role_type == "super_admin":

        # Check if the admin has sub-admins before deleting
        # if user.objects.filter(parent_admin=user).exists():
        #     messages.error(request, "Cannot delete admin with sub-admins.")
        #     return redirect('/accounts/')

        # Reassign sub-admins to the parent admin before deleting
        children=User.objects.filter(parent_admin=user)
        if user.parent_admin:
            children.update(parent_admin=user.parent_admin, level=user.parent_admin.level+1)
        else:
            children.update(parent_admin=None, level=0)

        user.delete()
        return redirect('/accounts/')
    else:
        messages.error(request, "You are not the parent admin of this user.")
        return redirect('/accounts/')


@login_required(login_url='/accounts/login/')
def edit_admin(request, id):

    user = get_object_or_404(User, id=id)
    # Security check
    if user.parent_admin != request.user and request.user.role_type != "super_admin":
        return redirect('/accounts/')

    if request.method == "POST":
        user.username = request.POST.get('username')
        user.role_type = request.POST.get('role_type')
        # user.level = request.POST.get('level')

        user.save()

        return redirect('/accounts/')

    return render(request, "accounts/update_user.html", {"user": user})

