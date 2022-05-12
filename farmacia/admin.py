import imp
from django.contrib import admin
from .models import Medicamento, Medico, Empleado, Prescripcion, ListaMedicamentos


# Register your models here.

admin.site.register(Medicamento)
admin.site.register(Medico)
admin.site.register(Empleado)
admin.site.register(Prescripcion)
admin.site.register(ListaMedicamentos)