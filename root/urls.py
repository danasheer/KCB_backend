"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from branches.views import BrancheListView, BrancheCreateView, BrancheUpdateView, BrancheDeleteView, FloorListView, FloorCreateView, FloorUpdateView, FloorDeleteView, DepartmentListView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView, PrintersListView, PrintersCreateView, PrintersUpdateView, PrintersDeleteView
from employees.views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, ComputerListView, ComputerCreateView, ComputerUpdateView, ComputerDeleteView, MonitorListView, MonitorCreateView, MonitorUpdateView, MonitorDeleteView, ScannerListView, ScannerCreateView, ScannerUpdateView, ScannerDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/login/", LoginView.as_view(), name="login"),

    #     BRANCHES
    path("api/branches/", BrancheListView.as_view(), name="branches"),
    #     path("api/branches/create/", BrancheCreateView.as_view(), name="create"),
    #     path("api/branches/update/<int:id>/",
    #          BrancheUpdateView.as_view(), name="update"),
    #     path("api/branches/delete/<int:pk>/",
    #          BrancheDeleteView.as_view(), name="delete"),


    #    FLOORS
    path("api/floors/", FloorListView.as_view(), name="floors"),
    #     path("api/floors/create/", FloorCreateView.as_view(), name="create"),
    #     path("api/floors/update/<int:pk>/",
    #          FloorUpdateView.as_view(), name="update"),
    #     path("api/floors/delete/<int:pk>/",
    #          FloorDeleteView.as_view(), name="delete"),


    #     path("api/employees/", EmployeeListView.as_view(), name="employees"),
    #     path("api/employees/create/", EmployeeCreateView.as_view(), name="create"),
    #     path("api/employees/update/<int:pk>/",
    #          EmployeeUpdateView.as_view(), name="update"),
    #     path("api/employees/delete/<int:pk>/",
    #          EmployeeDeleteView.as_view(), name="delete"),

    #     DEPARTMENTS
    path("api/departments/", DepartmentListView.as_view(), name="departments"),

    #     path("api/departments/create/", DepartmentCreateView.as_view(), name="create"),
    #     path("api/departments/update/<int:pk>/",
    #          DepartmentUpdateView.as_view(), name="update"),
    #     path("api/departments/delete/<int:pk>/",
    #          DepartmentDeleteView.as_view(), name="delete"),

    #     PRINTERS
    path("api/printers/", PrintersListView.as_view(), name="printers"),

    #     path("api/printers/create/", PrintersCreateView.as_view(), name="create"),
    #     path("api/printers/update/<int:pk>/",
    #          PrintersUpdateView.as_view(), name="update"),
    #     path("api/printers/delete/<int:pk>/",
    #          PrintersDeleteView.as_view(), name="delete"),

    #     COMPUTERS
    path("api/computers/", ComputerListView.as_view(), name="computers"),

    #     path("api/computers/create/", ComputerCreateView.as_view(), name="create"),
    #     path("api/computers/update/<int:pk>/",
    #          ComputerUpdateView.as_view(), name="update"),
    #     path("api/computers/delete/<int:pk>/",
    #          ComputerDeleteView.as_view(), name="delete"),

    #     MONITORS
    path("api/monitors/", MonitorListView.as_view(), name="monitors"),
    #     path("api/monitors/create/", MonitorCreateView.as_view(), name="create"),
    #     path("api/monitors/update/<int:pk>/",
    #          MonitorUpdateView.as_view(), name="update"),
    #     path("api/monitors/delete/<int:pk>/",
    #          MonitorDeleteView.as_view(), name="delete"),

    #     SCANNERS
    path("api/scanners/", ScannerListView.as_view(), name="scanners"),
    #     path("api/scanners/create/", ScannerCreateView.as_view(), name="create"),
    #     path("api/scanners/update/<int:pk>/",
    #          ScannerUpdateView.as_view(), name="update"),
    #     path("api/scanners/delete/<int:pk>/",
    #          ScannerDeleteView.as_view(), name="delete"),

]
