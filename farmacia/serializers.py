from rest_framework import serializers
from .models import Prescripcion, Medicamento

class PrescripcionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prescripcion
        fields = "__all__"

class MedicamentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medicamento
        fields = "__all__"
