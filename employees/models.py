from django.db import models
from branches.models import Branche, Floor


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    branch = models.ForeignKey(Branche, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Computer(models.Model):
    computername = models.CharField(max_length=255)
    macaddress = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    serialnumber = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    invontorynumber = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.computername} - {self.macaddress}"


class Monitor(models.Model):
    serialnumber = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    invontorynumber = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ip} - {self.serialnumber}"


class Scanner(models.Model):
    serialnumber = models.CharField(max_length=255)
    invontorynumber = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.ip} - {self.serialnumber}"
