from django.db import models

# TABLAS AUXILIARES

class TipoSangre(models.Model):
    tipo = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.tipo


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# ENTIDADES PRINCIPALES

class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tipo_sangre = models.ForeignKey(TipoSangre, on_delete=models.SET_NULL, null=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Medico(models.Model):

    TIPO_MEDICO_CHOICES = [
        ('PLANTA', 'Médico de planta'),
        ('CONSULTOR', 'Consultor externo'),
        ('RESIDENTE', 'Residente'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    tipo_medico = models.CharField(
        max_length=15, choices=TIPO_MEDICO_CHOICES, default='PLANTA'
    )

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"


# CONSULTAS Y RELACIONES

class ConsultaMedica(models.Model):

    ESTADO_CONSULTA_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En proceso'),
        ('FINALIZADA', 'Finalizada'),
        ('CANCELADA', 'Cancelada'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_consulta = models.DateTimeField()
    motivo = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    estado = models.CharField(
        max_length=15, choices=ESTADO_CONSULTA_CHOICES, default='PENDIENTE'
    )

    def __str__(self):
        return f"Consulta {self.id} - {self.paciente.nombre} ({self.estado})"


class Tratamiento(models.Model):
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    descripcion = models.TextField()
    duracion_dias = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Tratamiento {self.id} - Consulta {self.consulta.id}"


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class RecetaMedica(models.Model):
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dosis = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)

    def __str__(self):
        return f"Receta {self.id} - {self.medicamento.nombre}"
