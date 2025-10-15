from django.urls import path, include
from django.contrib import admin
from interfaz_clinica import views
from rest_framework import routers 
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


# 1. Definición de Rutas API (Router de DRF)
router = routers.DefaultRouter()
router.register(r'tiposangres', views.TipoSangreViewSet)
router.register(r'especialidades', views.EspecialidadViewSet)
router.register(r'pacientes', views.PacienteViewSet)
router.register(r'medicos', views.MedicoViewSet)
router.register(r'consultasmedicas', views.ConsultaMedicaViewSet)
router.register(r'tratamientos', views.TratamientoViewSet)
router.register(r'medicamentos', views.MedicamentoViewSet)
router.register(r'recetasmedicas', views.RecetaMedicaViewSet)


urlpatterns = [
    # 0. Ruta del administrador de Django
    path('admin/', admin.site.urls), 

    # Rutas API (CRÍTICO: Incluir el router)
    path('api/', include(router.urls)),

    # Páginas estáticas
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),

    # 4. RUTAS DE LA API (INCLUIR LAS URLS GENERADAS POR EL ROUTER)
    path('api/', include(router.urls)),
    
    # 5. RUTAS DE DOCUMENTACIÓN (SPECTACULAR)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # ========== TIPO SANGRE (CRUD) ==========
    path('tipos-sangre/', views.TipoSangreListView.as_view(), name='tiposangre_list'),
    path('tipos-sangre/nuevo/', views.TipoSangreCreateView.as_view(), name='tiposangre_create'),
    path('tipos-sangre/<int:pk>/editar/', views.TipoSangreUpdateView.as_view(), name='tiposangre_update'),
    path('tipos-sangre/<int:pk>/eliminar/', views.TipoSangreDeleteView.as_view(), name='tiposangre_delete'),

    # ========== ESPECIALIDAD (CRUD) ==========
    path('especialidades/', views.EspecialidadListView.as_view(), name='especialidad_list'),
    path('especialidades/nueva/', views.EspecialidadCreateView.as_view(), name='especialidad_create'),
    path('especialidades/<int:pk>/editar/', views.EspecialidadUpdateView.as_view(), name='especialidad_update'),
    path('especialidades/<int:pk>/eliminar/', views.EspecialidadDeleteView.as_view(), name='especialidad_delete'),

    # ========== PACIENTE (CRUD) ==========
    path('pacientes/', views.PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/', views.PacienteDeleteView.as_view(), name='paciente_delete'),

    # ========== MÉDICO (CRUD) ==========
    path('medicos/', views.MedicoListView.as_view(), name='medico_list'),
    path('medicos/nuevo/', views.MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/editar/', views.MedicoUpdateView.as_view(), name='medico_update'),
    path('medicos/<int:pk>/eliminar/', views.MedicoDeleteView.as_view(), name='medico_delete'),

    # ========== CONSULTA MÉDICA (CRUD) ==========
    path('consultas/', views.ConsultaMedicaListView.as_view(), name='consultamedica_list'),
    path('consultas/nueva/', views.ConsultaMedicaCreateView.as_view(), name='consultamedica_create'),
    path('consultas/<int:pk>/editar/', views.ConsultaMedicaUpdateView.as_view(), name='consultamedica_update'),
    path('consultas/<int:pk>/eliminar/', views.ConsultaMedicaDeleteView.as_view(), name='consultamedica_delete'),

    # ========== TRATAMIENTO (CRUD) ==========
    path('tratamientos/', views.TratamientoListView.as_view(), name='tratamiento_list'),
    path('tratamientos/nuevo/', views.TratamientoCreateView.as_view(), name='tratamiento_create'),
    path('tratamientos/<int:pk>/editar/', views.TratamientoUpdateView.as_view(), name='tratamiento_update'),
    path('tratamientos/<int:pk>/eliminar/', views.TratamientoDeleteView.as_view(), name='tratamiento_delete'),

    # ========== MEDICAMENTO (CRUD) ==========
    path('medicamentos/', views.MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamentos/nuevo/', views.MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('medicamentos/<int:pk>/editar/', views.MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamentos/<int:pk>/eliminar/', views.MedicamentoDeleteView.as_view(), name='medicamento_delete'),

    # ========== RECETA MÉDICA (CRUD) ==========
    path('recetas/', views.RecetaMedicaListView.as_view(), name='recetamedica_list'),
    path('recetas/nueva/', views.RecetaMedicaCreateView.as_view(), name='recetamedica_create'),
    path('recetas/<int:pk>/editar/', views.RecetaMedicaUpdateView.as_view(), name='recetamedica_update'),
    path('recetas/<int:pk>/eliminar/', views.RecetaMedicaDeleteView.as_view(), name='recetamedica_delete'),
]