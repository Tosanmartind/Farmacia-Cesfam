from django.shortcuts import render

# Stock.
def login(request):
    return render(request, "login.html")
# Medico.
def consultaMedicamentos(request):
    return render(request, "medico/consulta_medicamento.html")
def recetas(request):
    return render(request, "medico/recetas.html")
def generarPrescripciones(request):
    return render(request, "medico/generar_prescripcion.html")
# Farmacia.
def recepcionEntrega(request):
    return render(request, "farmacia/recepcion_entrega.html")
def recepcionFarmacia(request):
    return render(request, "farmacia/recepcion_farmacia.html")
# Stock.
def adminInventario(request):
    return render(request, "stock/stockAdmin_inventario.html")
def agregarMedicamentos(request):
    return render(request, "stock/agregar_medicamentos.html")
def modificarMedicamentos(request):
    return render(request, "stock/modificar_medicamentos.html")