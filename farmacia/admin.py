from django.contrib import admin
from .models import Medicamento, Medico

# Register your models here.

admin.site.register(Medicamento)
admin.site.register(Medico)