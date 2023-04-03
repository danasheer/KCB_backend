from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()


class Branche(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Floor(models.Model):
    number = models.IntegerField()
    branch = models.ForeignKey(Branche, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number}"


class department(models.Model):
    name = models.CharField(max_length=255)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class printer(models.Model):
    ip = models.CharField(max_length=255)
    serialnumber = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    invontorynumber = models.CharField(max_length=255)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ip} - {self.serialnumber}"
