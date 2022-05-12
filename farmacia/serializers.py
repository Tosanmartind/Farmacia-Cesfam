from rest_framework import serializers
from .models import Prescripcion, ListaMedicamentos, Medicamento

class PrescripcionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prescripcion
        fields = ['prescripcion_id', 'medico', 'paciente', 'correo', 'telefono', 'fecha_entrega', 'fecha_expira']

class MedicamentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medicamento
        fields = ['codigo', 'descripcion', 'fabricante', 'contenido', 'gramaje', 'cantidad']

class ListaMedicamentosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ListaMedicamentos
        fields = ['lista_id', 'prescripcion', 'medicamento', 'comprimidos', 'frecuencia_hrs', 'dias_tratamiento']