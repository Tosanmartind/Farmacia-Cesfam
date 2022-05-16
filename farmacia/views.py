from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from .models import Medicamento, Empleado, Prescripcion, Medico
from .forms import NewUserForm
#REST
import requests

#REST Framework
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PrescripcionSerializer, MedicamentoSerializer

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
                return render(request, "farmacia/recepcion_farmacia.html")
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
    response=requests.get('http://127.0.0.1:8000/apiprescripciones').json()
    return render(request, "medico/recetas.html", {"response": response})

def generarPrescripciones(request):
    if request.method == 'GET':
        response=requests.get('http://127.0.0.1:8000/apiprescripciones').json()
        return render(request, "medico/generar_prescripcion.html", {"response": response})
    if request.method == 'POST':

        paciente = request.POST['txtPaciente']
        correo = request.POST['txtCorreo']
        telefono = request.POST['numTelefono']
        fecha_entrega = request.POST['fechaEntrega']
        fecha_expira = request.POST['fechaExp']
        comprimidos = request.POST['numCantidad']
        frecuencia_hrs = request.POST['numFrecuencia']
        dias_tratamiento = request.POST['numDias']

        rutMedico = request.POST['txtMedico']
        medico = Medico.objects.get(rut=rutMedico)

        nameMedicamento = request.POST['txtMedicamento']
        medicamento = Medicamento.objects.get(descripcion=nameMedicamento)
    
        prescripcion = Prescripcion.objects.create(medico=medico, paciente=paciente, correo=correo, telefono=telefono, fecha_entrega=fecha_entrega, fecha_expira=fecha_expira, medicamento=medicamento, comprimidos=comprimidos, frecuencia_hrs=frecuencia_hrs, dias_tratamiento=dias_tratamiento)
        return redirect('prescripciones')

# Farmacia.
def recepcionEntrega(request, codigo):
    if request.method == 'GET':
        prescripcion = Prescripcion.objects.get(prescripcion_id=codigo)
        return render(request, "farmacia/recepcion_entrega.html", {"prescripcion": prescripcion})
    
    if request.method == 'POST':
        """
        medicamento = request.POST['txtMedicamento']
        correo = request.POST['txtCorreo']
        telefono = request.POST['numTelefono']

        """
        return redirect('recepcion-farmacia')
    
def recepcionFarmacia(request):
    if request.method == 'GET':
        prescripcionListar = Prescripcion.objects.select_related('medicamento')
        return render(request, "farmacia/recepcion_farmacia.html", {"prescripcion": prescripcionListar})

def recepcionEliminar(request, codigo):
    prescripcion = Prescripcion.objects.get(prescripcion_id=codigo)
    prescripcion.delete()
    return redirect('recepcion-farmacia')
# Stock.
def adminInventario(request):
    medicamentoListar = Medicamento.objects.all()
    return render(request, "stock/stockAdmin_inventario.html", {"medicamento": medicamentoListar})

def agregarMedicamentos(request):
    if request.method == 'GET':
        return render(request, "stock/agregar_medicamentos.html")
    if request.method == 'POST':
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

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

@api_view(["GET"])
def prescripciones(request):
    presquery = Prescripcion.objects.all()
    medquery = Medicamento.objects.all()
    ObjPrescripcionSerializer = PrescripcionSerializer(presquery, many=True)
    ObjMedicamentoSerializer = MedicamentoSerializer(medquery, many=True)
    ResultModel = ObjPrescripcionSerializer.data+ObjMedicamentoSerializer.data
    return Response(ResultModel)

