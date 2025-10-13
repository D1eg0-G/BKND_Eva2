from django.contrib import admin
from .models import TipoSangre, Especialidad, Paciente, Medico, ConsultaMedica, RecetaMedica, Tratamiento, Medicamento
# Register your models here.
admin.site.register(TipoSangre)
admin.site.register(Especialidad)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(ConsultaMedica)
admin.site.register(RecetaMedica)
admin.site.register(Tratamiento)
admin.site.register(Medicamento)