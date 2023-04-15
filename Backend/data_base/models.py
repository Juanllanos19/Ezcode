from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidoPat = models.CharField(max_length=50)
    apellidoMat = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    correo = models.EmailField()
    contrasena = models.CharField('Contraseña', max_length=500)
    def __str__(self) :
        return self.nombre + ' ' + self.apellidoPat + ' ' + self.apellidoMat

class Periodo(models.Model):
    fechaInicio = models.DateField('Fecha de inicio')
    fechaFin = models.DateField('Fecha de fin')
    def __str__(self) -> str:
        return self.fechaInicio + ' - ' + self.fechaFin

class Tema(models.Model):
    tipo: models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.tipo
    
class Pregunta(models.Model):
    titulo = models.CharField(max_length=500)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    contenido = models.JSONField(upload_to = 'data_base/JSONdoc/')
    def __str__(self) -> str:
        return self.titulo

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidoPat = models.CharField(max_length=50)
    apellidoMat = models.CharField(max_length=50)
    correo = models.EmailField()
    contrasena = models.CharField('Contraseña', max_length=500)
    def __str__(self) :
        return self.nombre + ' ' + self.apellidoPat + ' ' + self.apellidoMat
    
class Actividad(models.Model):
    nombre = models.CharField(max_length=500)
    fechaInicio = models.DateField('Fecha de inicio')
    fechaFin = models.DateField('Fecha de fin')
    duracion = models.DurationField()
    pregunta = models.ManyToManyField(Pregunta)
    def __str__(self) -> str:
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=500)
    uf = models.CharField(max_length=15)
    cupo = models.IntegerField()
    estado = models.BooleanField()
    profesor = models.ManyToManyField(Profesor)
    periodo = models.ForeignKey(Periodo)
    actividad = models.ManyToManyField(Actividad)
    def __str__(self) -> str:
        return self.nombre + '.' + self.uf
    
class Carrera(models.Model):
    siglas = models.CharField(max_length=3)
    def __str__(self) -> str:
        return self.siglas

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidoPat = models.CharField(max_length=50)
    apellidoMat = models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=9)
    correo = models.EmailField()
    contrasena = models.CharField('Contraseña', max_length=500)
    calificacion = models.ManyToManyField(Actividad, through='Calificacion')
    def __str__(self) -> str:
        return self.matricula + ': ' + self.nombre + ' ' + self.apellidoPat

class Calificacion(models.Model):
    actividades = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='calificaciones')
    calificacion = models.IntegerField(default=0)
    comentario = models.TextField()
    def __str__(self) -> str:
        return str(self.calificacion) + ' ' + self.comentario