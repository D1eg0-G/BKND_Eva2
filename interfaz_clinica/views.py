# views.py
from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import *
from .filters import *
from .serializer import *

# Vistas para páginas estáticas
def home(request):
    return render(request, 'home.html')

def contacto(request):
    if request.method == 'POST':
        # Procesar formulario de contacto
        messages.success(request, 'Mensaje enviado correctamente')
    return render(request, 'contacto.html')

def servicios(request):
    return render(request, 'servicios.html')

# VISTAS BASADAS EN CLASES CON FILTROS Y CONTEXTOS

# ========== TIPO SANGRE ==========
class TipoSangreListView(FilterView):
    model = TipoSangre
    filterset_class = TipoSangreFilter
    template_name = 'modelos/tiposangre.html'
    context_object_name = 'filter'
    paginate_by = 10

class TipoSangreCreateView(SuccessMessageMixin, CreateView):
    model = TipoSangre
    template_name = 'modelos/tiposangre.html'
    fields = ['tipo']
    success_url = reverse_lazy('tiposangre_list')
    success_message = "Tipo de sangre creado exitosamente"

class TipoSangreUpdateView(SuccessMessageMixin, UpdateView):
    model = TipoSangre
    template_name = 'modelos/tiposangre.html'
    fields = ['tipo']
    success_url = reverse_lazy('tiposangre_list')
    success_message = "Tipo de sangre actualizado exitosamente"

class TipoSangreDeleteView(DeleteView):
    model = TipoSangre
    template_name = 'modelos/tiposangre.html'
    success_url = reverse_lazy('tiposangre_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Tipo de sangre eliminado exitosamente")
        return super().delete(request, *args, **kwargs)

# ========== ESPECIALIDAD ==========
class EspecialidadListView(FilterView):
    model = Especialidad
    filterset_class = EspecialidadFilter
    template_name = 'modelos/especialidad.html'
    context_object_name = 'filter'
    paginate_by = 10

class EspecialidadCreateView(SuccessMessageMixin, CreateView):
    model = Especialidad
    template_name = 'modelos/especialidad.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('especialidad_list')
    success_message = "Especialidad creada exitosamente"

class EspecialidadUpdateView(SuccessMessageMixin, UpdateView):
    model = Especialidad
    template_name = 'modelos/especialidad.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('especialidad_list')
    success_message = "Especialidad actualizada exitosamente"
    def get_object(self, queryset=None):
        # Esta función busca la PK en la URL (que es lo que hace el UpdateView por defecto)
        # Si tu URL es /especialidades/5/editar/, la PK (5) se pasa automáticamente
        return super().get_object(queryset)

class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = 'modelos/especialidad.html'
    success_url = reverse_lazy('especialidad_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Especialidad eliminada exitosamente")
        return super().delete(request, *args, **kwargs)

# ========== PACIENTE ==========
class PacienteListView(FilterView):
    model = Paciente
    filterset_class = PacienteFilter
    template_name = 'modelos/paciente.html'
    context_object_name = 'filter'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipos_sangre'] = TipoSangre.objects.all()
        return context

class PacienteCreateView(SuccessMessageMixin, CreateView):
    model = Paciente
    template_name = 'modelos/paciente.html'
    fields = ['rut', 'nombre', 'apellido', 'fecha_nacimiento', 'tipo_sangre', 
            'correo', 'telefono', 'direccion', 'activo']
    success_url = reverse_lazy('paciente_list')
    success_message = "Paciente creado exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipos_sangre'] = TipoSangre.objects.all()
        return context

class PacienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Paciente
    template_name = 'modelos/paciente.html'
    fields = ['rut', 'nombre', 'apellido', 'fecha_nacimiento', 'tipo_sangre', 
            'correo', 'telefono', 'direccion', 'activo']
    success_url = reverse_lazy('paciente_list')
    success_message = "Paciente actualizado exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipos_sangre'] = TipoSangre.objects.all()
        return context

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'modelos/paciente.html'
    success_url = reverse_lazy('paciente_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Paciente eliminado exitosamente")
        return super().delete(request, *args, **kwargs)

# ========== MÉDICO ==========
class MedicoListView(FilterView):
    model = Medico
    filterset_class = MedicoFilter
    template_name = 'modelos/medico.html'
    context_object_name = 'filter'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidades'] = Especialidad.objects.all()
        return context

class MedicoCreateView(SuccessMessageMixin, CreateView):
    model = Medico
    template_name = 'modelos/medico.html'
    fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'activo', 
            'especialidad', 'tipo_medico']
    success_url = reverse_lazy('medico_list')
    success_message = "Médico creado exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidades'] = Especialidad.objects.all()
        return context

class MedicoUpdateView(SuccessMessageMixin, UpdateView):
    model = Medico
    template_name = 'modelos/medico.html'
    fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'activo', 
            'especialidad', 'tipo_medico']
    success_url = reverse_lazy('medico_list')
    success_message = "Médico actualizado exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidades'] = Especialidad.objects.all()
        return context

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'modelos/medico.html'
    success_url = reverse_lazy('medico_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Médico eliminado exitosamente")
        return super().delete(request, *args, **kwargs)

# ========== CONSULTA MÉDICA ==========
class ConsultaMedicaListView(FilterView):
    model = ConsultaMedica
    filterset_class = ConsultaMedicaFilter
    template_name = 'modelos/consultamedica.html'
    context_object_name = 'filter'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        context['medicos'] = Medico.objects.all()
        return context

class ConsultaMedicaCreateView(SuccessMessageMixin, CreateView):
    model = ConsultaMedica
    template_name = 'modelos/consultamedica.html'
    fields = ['paciente', 'medico', 'fecha_consulta', 'motivo', 'diagnostico', 'estado']
    success_url = reverse_lazy('consultamedica_list')
    success_message = "Consulta médica creada exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        context['medicos'] = Medico.objects.all()
        return context

class ConsultaMedicaUpdateView(SuccessMessageMixin, UpdateView):
    model = ConsultaMedica
    template_name = 'modelos/consultamedica.html'
    fields = ['paciente', 'medico', 'fecha_consulta', 'motivo', 'diagnostico', 'estado']
    success_url = reverse_lazy('consultamedica_list')
    success_message = "Consulta médica actualizada exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        context['medicos'] = Medico.objects.all()
        return context

class ConsultaMedicaDeleteView(DeleteView):
    model = ConsultaMedica
    template_name = 'modelos/consultamedica.html'
    success_url = reverse_lazy('consultamedica_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Consulta médica eliminada exitosamente")
        return super().delete(request, *args, **kwargs)

# ========== TRATAMIENTO ==========
class TratamientoListView(FilterView):
    model = Tratamiento
    filterset_class = TratamientoFilter
    template_name = 'modelos/tratamiento.html'
    context_object_name = 'filter'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultas'] = ConsultaMedica.objects.all()
        return context

class TratamientoCreateView(SuccessMessageMixin, CreateView):
    model = Tratamiento
    template_name = 'modelos/tratamiento.html'
    fields = ['consulta', 'descripcion', 'duracion_dias', 'observaciones']
    success_url = reverse_lazy('tratamiento_list')
    success_message = "Tratamiento creado exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultas'] = ConsultaMedica.objects.all()
        return context

class TratamientoUpdateView(SuccessMessageMixin, UpdateView):
    model = Tratamiento
    template_name = 'modelos/tratamiento.html'
    fields = ['consulta', 'descripcion', 'duracion_dias', 'observaciones']
    success_url = reverse_lazy('tratamiento_list')
    success_message = "Tratamiento actualizado exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultas'] = ConsultaMedica.objects.all()
        return context

class TratamientoDeleteView(DeleteView):
    model = Tratamiento
    template_name = 'modelos/tratamiento.html'
    success_url = reverse_lazy('tratamiento_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Tratamiento eliminado exitosamente")
        return super().delete(request, *args, **kwargs)

# ========== MEDICAMENTO ==========
class MedicamentoListView(FilterView):
    model = Medicamento
    filterset_class = MedicamentoFilter
    template_name = 'modelos/medicamento.html'
    context_object_name = 'filter'
    paginate_by = 10

class MedicamentoCreateView(SuccessMessageMixin, CreateView):
    model = Medicamento
    template_name = 'modelos/medicamento.html'
    fields = ['nombre', 'laboratorio', 'stock', 'precio_unitario']
    success_url = reverse_lazy('medicamento_list')
    success_message = "Medicamento creado exitosamente"

class MedicamentoUpdateView(SuccessMessageMixin, UpdateView):
    model = Medicamento
    template_name = 'modelos/medicamento.html'
    fields = ['nombre', 'laboratorio', 'stock', 'precio_unitario']
    success_url = reverse_lazy('medicamento_list')
    success_message = "Medicamento actualizado exitosamente"

class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = 'modelos/medicamento.html'
    success_url = reverse_lazy('medicamento_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Medicamento eliminado exitosamente")
        return super().delete(request, *args, **kwargs)

# ========== RECETA MÉDICA ==========
class RecetaMedicaListView(FilterView):
    model = RecetaMedica
    filterset_class = RecetaMedicaFilter
    template_name = 'modelos/recetamedica.html'
    context_object_name = 'filter'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tratamientos'] = Tratamiento.objects.all()
        context['medicamentos'] = Medicamento.objects.all()
        return context

class RecetaMedicaCreateView(SuccessMessageMixin, CreateView):
    model = RecetaMedica
    template_name = 'modelos/recetamedica.html'
    fields = ['tratamiento', 'medicamento', 'dosis', 'frecuencia', 'duracion']
    success_url = reverse_lazy('recetamedica_list')
    success_message = "Receta médica creada exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tratamientos'] = Tratamiento.objects.all()
        context['medicamentos'] = Medicamento.objects.all()
        return context

class RecetaMedicaUpdateView(SuccessMessageMixin, UpdateView):
    model = RecetaMedica
    template_name = 'modelos/recetamedica.html'
    fields = ['tratamiento', 'medicamento', 'dosis', 'frecuencia', 'duracion']
    success_url = reverse_lazy('recetamedica_list')
    success_message = "Receta médica actualizada exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tratamientos'] = Tratamiento.objects.all()
        context['medicamentos'] = Medicamento.objects.all()
        return context

class RecetaMedicaDeleteView(DeleteView):
    model = RecetaMedica
    template_name = 'modelos/recetamedica.html'
    success_url = reverse_lazy('recetamedica_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Receta médica eliminada exitosamente")
        return super().delete(request, *args, **kwargs)

# ========== VIEWSETS PARA DRF (MANTENER TUS EXISTENTES) ==========
class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class TipoSangreViewSet(viewsets.ModelViewSet):
    queryset = TipoSangre.objects.all()
    serializer_class = TipoSangreSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class RecetaMedicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']