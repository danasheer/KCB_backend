from django.db import models
from branches.models import Branche, Floor, Department


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="employees")

    def __str__(self):
        return self.name


class Computer(models.Model):
    computername = models.CharField(max_length=255)
    macaddress = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    serialnumber = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    invontorynumber = models.CharField(max_length=255)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="computers")

    def __str__(self):
        return f"{self.computername} - {self.macaddress}"


class Monitor(models.Model):
    serialnumber = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    invontorynumber = models.CharField(max_length=255)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="monitors")

    def __str__(self):
        return f"{self.ip} - {self.serialnumber}"


class Scanner(models.Model):
    serialnumber = models.CharField(max_length=255)
    invontorynumber = models.CharField(max_length=255)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="scanners")

    def __str__(self):

        return f" {self.serialnumber}"
