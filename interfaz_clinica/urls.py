from django.urls import path, include
from rest_framework import routers
from .views import (
    TipoSangreViewSet,
    EspecialidadViewSet,
    PacienteViewSet,
    MedicoViewSet,
    ConsultaMedicaViewSet,
    TratamientoViewSet,
    MedicamentoViewSet,
    RecetaMedicaViewSet,


)

router = routers.DefaultRouter()
router.register(r'tiposangres', TipoSangreViewSet)
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'consultasmedicas', ConsultaMedicaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'recetasmedicas', RecetaMedicaViewSet)

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),
]

