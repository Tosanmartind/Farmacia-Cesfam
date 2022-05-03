from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('consulta-medicamentos', views.consultaMedicamentos, name="medicamentos"),
    path('recetas', views.recetas, name="prescripciones"),
    path('generar-prescripciones', views.generarPrescripciones, name="generar-presecipciones"),
    path('recepcion-farmacia', views.recepcionFarmacia, name="recepcion-farmacia"),
    path('recepcion-entrega', views.recepcionEntrega, name="recepcion-entrega"),
    path('inventario', views.adminInventario, name="inventario"),
    path('agregar-medicamentos', views.agregarMedicamentos, name="agregar-medicamentos"),
    path('modificar-medicamentos', views.modificarMedicamentos, name="modificar-medicamentos")
]
