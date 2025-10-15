from rest_framework import serializers
from .models import (
    Especialidad, Paciente, Medico, TipoSangre,
    ConsultaMedica, Tratamiento, Medicamento, RecetaMedica
)

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('id', 'nombre', 'descripcion')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('id','rut', 'nombre', 'apellido', 'fecha_nacimiento', 'tipo_sangre', 'correo','telefono','direccion','activo')

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id','nombre','apellido','rut','correo','telefono','activo', 'especialidad', 'tipo_medico')

class TipoSangreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSangre
        fields = ('id', 'tipo')

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = ('id','paciente', 'medico', 'fecha_consulta','motivo','diagnostico','estado')

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = ('id', 'consulta', 'descripcion', 'duracion_dias','observaciones')

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ('id','nombre','laboratorio','stock','precio_unitario')

class RecetaMedicaSerializer(serializers.ModelSerializer):
    tratamiento_nombre = serializers.CharField(source='tratamiento.__str__', read_only=True)
    medicamento_nombre = serializers.CharField(source='medicamento.__str__', read_only=True)

    class Meta:
        model = RecetaMedica
        fields = (
            'id', 
            'tratamiento', 
            'medicamento', 
            'dosis', 
            'frecuencia', 
            'duracion',
            # Incluir los campos personalizados aquí:
            'tratamiento_nombre', 
            'medicamento_nombre'
        )