from django.contrib import admin
from .models import Branche, Floor, department, printer


admin.site.register(Branche)
admin.site.register(Floor)
admin.site.register(department)
admin.site.register(printer)


# Register your models here.
