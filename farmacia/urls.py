from django.urls import path
from . import views

urlpatterns = [
    # Login.
    path('', views.login, name="login"),
    # Medico.
    path('consulta-medicamentos', views.consultaMedicamentos, name="medicamentos"),
    path('recetas', views.recetas, name="prescripciones"),
    path('generar-prescripciones', views.generarPrescripciones, name="generar-presecipciones"),
    # Farmacia.
    path('recepcion-farmacia', views.recepcionFarmacia, name="recepcion-farmacia"),
    path('recepcion-entrega', views.recepcionEntrega, name="recepcion-entrega"),
    # Stock.
    path('inventario', views.adminInventario, name="inventario"),
    path('agregar-medicamentos', views.agregarMedicamentos, name="agregar-medicamentos"),
    path('modificar-medicamentos/<codigo>', views.modificarMedicamentos, name="modificar-medicamentos"),
    path('eliminarMedicamentos/<codigo>', views.eliminarMedicamentos),
]
