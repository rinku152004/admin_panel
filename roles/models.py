from django.db import models

class Role(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Permission(models.Model):

    name = models.CharField(max_length=100)

    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RolePermission(models.Model):

    role = models.ForeignKey(Role,on_delete=models.CASCADE)

    permission = models.ForeignKey(Permission,on_delete=models.CASCADE)