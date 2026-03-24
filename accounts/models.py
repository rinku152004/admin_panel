# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_TYPES = (
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('sub_admin', 'Sub Admin'),
    )

    role_type = models.CharField(max_length=20, choices=ROLE_TYPES)

    parent_admin = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children_admins'
    )

    is_active_admin = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=0)


    def __str__(self):
        return self.username
    
class Permission(models.Model):

    name = models.CharField(max_length=100)

    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Role(models.Model):

    name = models.CharField(max_length=100)

    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name