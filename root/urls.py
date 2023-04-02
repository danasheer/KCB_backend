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
from branches.views import BrancheListView, BrancheCreateView, BrancheUpdateView, BrancheDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/login/", LoginView.as_view(), name="login"),
    path("api/branches/", BrancheListView.as_view(), name="branches"),
    path("api/branches/create/", BrancheCreateView.as_view(), name="create"),
    path("api/branches/update/<int:pk>/",
         BrancheUpdateView.as_view(), name="update"),
    path("api/branches/delete/<int:pk>/",
         BrancheDeleteView.as_view(), name="delete"),

]
