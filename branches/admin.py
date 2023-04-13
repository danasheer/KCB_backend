from django.contrib import admin
from .models import Branche, Floor, Department, printer


admin.site.register(Branche)
admin.site.register(Floor)
admin.site.register(Department)
admin.site.register(printer)


# Register your models here.
