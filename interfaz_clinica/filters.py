import django_filters
from django import forms
from .models import *

class TipoSangreFilter(django_filters.FilterSet):
    tipo = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por tipo...'})
    )

    class Meta:
        model = TipoSangre
        fields = ['tipo']

class EspecialidadFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre...'})
    )

    class Meta:
        model = Especialidad
        fields = ['nombre']

class PacienteFilter(django_filters.FilterSet):
    rut = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por RUT...'})
    )
    nombre = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre...'})
    )
    apellido = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por apellido...'})
    )
    tipo_sangre = django_filters.ModelChoiceFilter(
        queryset=TipoSangre.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    activo = django_filters.BooleanFilter(
        widget=forms.Select(choices=[('', 'Todos'), ('true', 'Sí'), ('false', 'No')],
                        attrs={'class': 'form-control'})
    )

    class Meta:
        model = Paciente
        fields = ['rut', 'nombre', 'apellido', 'tipo_sangre', 'activo']

class MedicoFilter(django_filters.FilterSet):
    rut = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por RUT...'})
    )
    nombre = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre...'})
    )
    apellido = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por apellido...'})
    )
    especialidad = django_filters.ModelChoiceFilter(
        queryset=Especialidad.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tipo_medico = django_filters.ChoiceFilter(
        choices=Medico.TIPO_MEDICO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    activo = django_filters.BooleanFilter(
        widget=forms.Select(choices=[('', 'Todos'), ('true', 'Sí'), ('false', 'No')],
                        attrs={'class': 'form-control'})
    )

    class Meta:
        model = Medico
        fields = ['rut', 'nombre', 'apellido', 'especialidad', 'tipo_medico', 'activo']

class ConsultaMedicaFilter(django_filters.FilterSet):
    paciente = django_filters.ModelChoiceFilter(
        queryset=Paciente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    medico = django_filters.ModelChoiceFilter(
        queryset=Medico.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    estado = django_filters.ChoiceFilter(
        choices=ConsultaMedica.ESTADO_CONSULTA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    fecha_desde = django_filters.DateFilter(
        field_name='fecha_consulta',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    fecha_hasta = django_filters.DateFilter(
        field_name='fecha_consulta',
        lookup_expr='lte',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = ConsultaMedica
        fields = ['paciente', 'medico', 'estado', 'fecha_consulta']

class TratamientoFilter(django_filters.FilterSet):
    consulta = django_filters.ModelChoiceFilter(
        queryset=ConsultaMedica.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Tratamiento
        fields = ['consulta']

class MedicamentoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre...'})
    )
    laboratorio = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por laboratorio...'})
    )
    stock_min = django_filters.NumberFilter(
        field_name='stock',
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock mínimo'})
    )

    class Meta:
        model = Medicamento
        fields = ['nombre', 'laboratorio', 'stock']

class RecetaMedicaFilter(django_filters.FilterSet):
    tratamiento = django_filters.ModelChoiceFilter(
        queryset=Tratamiento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    medicamento = django_filters.ModelChoiceFilter(
        queryset=Medicamento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = RecetaMedica
        fields = ['tratamiento', 'medicamento']