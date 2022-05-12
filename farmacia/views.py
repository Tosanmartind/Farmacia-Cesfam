from pydoc import describe
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.db import connection
from .models import Medicamento, Empleado, Prescripcion, ListaMedicamentos, Medico
from .forms import NewUserForm
#REST
import requests

#REST Framework
from rest_framework import viewsets
from .serializers import PrescripcionSerializer, MedicamentoSerializer, ListaMedicamentosSerializer

# Login.
def login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            
            # Save session as cookie to login the user
            login_auth(request, user)
            # Success, now let's login the user.    
            cargo = Empleado.get_cargo(user.pk)
            if cargo == 'M':
                medicamentoListar=requests.get('http://127.0.0.1:8000/api/medicamentos/').json()
                return render(request, "medico/consulta_medicamento.html", {"response": medicamentoListar})
            elif cargo == 'F':
                prescripcionListar = ListaMedicamentos.objects.select_related('prescripcion', 'medicamento')
                return render(request, "farmacia/recepcion_farmacia.html", {"prescripcion": prescripcionListar})
            elif cargo == 'A':
                medicamentoListar = Medicamento.objects.all()
                return render(request, "stock/stockAdmin_inventario.html", {"medicamento": medicamentoListar})
            else:
                return render(request,'invitado/index.html')
            
        else:
            return render(request,'login.html',{'error_message': 'Contraseña O Usuario Incorrecto'} )   
    else:
        return render(request, 'login.html')
# Logout
def logout(request):
    logout_auth(request)
    return redirect('/login')
def invitado(request):
    return render(request,'invitado/index.html')
# Registrar
def register(request):
    form = NewUserForm()

    if request.method== 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    data = {'form':form}
    return render(request,'registrar.html',data)        
# Medico (Consumo api).
def consultaMedicamentos(request):
    response=requests.get('http://127.0.0.1:8000/api/medicamentos/').json()
    return render(request, "medico/consulta_medicamento.html", {"response": response})

def recetas(request):
    response=requests.get('http://127.0.0.1:8000/api/prescripciones/').json()
    return render(request, "medico/recetas.html", {"response": response})

def generarPrescripciones(request):
    return render(request, "medico/generar_prescripcion.html")

# Farmacia.
def recepcionEntrega(request):
    return render(request, "farmacia/recepcion_entrega.html")

def recepcionFarmacia(request):
    if request.method == 'GET':
        prescripcionListar = ListaMedicamentos.objects.select_related('prescripcion', 'medicamento')
        return render(request, "farmacia/recepcion_farmacia.html", {"prescripcion": prescripcionListar})

# Stock.
def adminInventario(request):
    medicamentoListar = Medicamento.objects.all()
    return render(request, "stock/stockAdmin_inventario.html", {"medicamento": medicamentoListar})

def agregarMedicamentos(request):
    if request.method == 'GET':
        return render(request, "stock/agregar_medicamentos.html")
    elif request.method == 'POST':
        descripcion	= request.POST['txtDescripcion']
        fabricante = request.POST['txtFabricante'] 
        contenido = request.POST['numContenido'] 
        gramaje	= request.POST['numGramaje'] 
        precio = request.POST['numPrecio'] 
        cantidad = request.POST['numCantidad']

        medicamento = Medicamento.objects.create(descripcion=descripcion, fabricante=fabricante, contenido=contenido, gramaje=gramaje, precio=precio, cantidad=cantidad)
        return redirect('inventario')

def eliminarMedicamentos(request, codigo):
    medicamento = Medicamento.objects.get(codigo=codigo)
    medicamento.delete()
    return redirect('inventario')


def modificarMedicamentos(request, codigo):
    if request.method == 'GET':
        medicamentoModificar = Medicamento.objects.get(codigo=codigo)
        return render(request, "stock/modificar_medicamentos.html", {"medicamento": medicamentoModificar})
    elif request.method == 'POST':
        codigo	= request.POST['numCodigo']
        descripcion	= request.POST['txtDescripcion']
        fabricante = request.POST['txtFabricante'] 
        contenido = request.POST['numContenido'] 
        gramaje	= request.POST['numGramaje'] 
        precio = request.POST['numPrecio'] 
        cantidad = request.POST['numCantidad']

        medicamento = Medicamento.objects.get(codigo=codigo)
        medicamento.descripcion = descripcion
        medicamento.fabricante = fabricante
        medicamento.contenido = contenido
        medicamento.gramaje = gramaje
        medicamento.precio = precio
        medicamento.cantidad = cantidad
        medicamento.save()  

        return redirect('inventario')

#REST Framework viewsets

class PrescripcionViewSet(viewsets.ModelViewSet):
    queryset = Prescripcion.objects.all()
    serializer_class = PrescripcionSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class ListaMedicamentosViewSet(viewsets.ModelViewSet):
    queryset = ListaMedicamentos.objects.all()
    serializer_class = ListaMedicamentosSerializer