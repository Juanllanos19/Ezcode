from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=256)
    def __str__(self) :
        return self.nombre

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    apellidoPat = models.CharField(max_length=250)
    apellidoMat = models.CharField(max_length=250)
    especialidad = models.CharField(max_length=250)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    correo = models.EmailField()
    contrasena = models.CharField('Contraseña', max_length=500)
    def __str__(self) :
        return self.nombre + ' ' + self.apellidoPat + ' ' + self.apellidoMat

class Periodo(models.Model):
    fechaInicio = models.DateField('Fecha de inicio')
    fechaFin = models.DateField('Fecha de fin')
    def __str__(self) :
        return str(self.fechaInicio) + ' | ' + str(self.fechaFin)

class Tema(models.Model):
    nombre = models.CharField(max_length=250)
    tipo = models.TextField('subtema')
    def __str__(self) :
        return self.nombre + ': ' + str(self.tipo)
    
class Dificultad(models.Model):
    rango = models.CharField(max_length=20)
    def __str__(self) :
        return self.rango
    
class Pregunta(models.Model):
    titulo = models.CharField(max_length=500)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    contenido = models.FileField(upload_to = 'data_base/JSONdoc/')
    tipoP = models.BooleanField("tipo de pregunta | Abierta 0 | Cerrada 1", default=0)
    estado = models.BooleanField(default=0)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    dificultad = models.ForeignKey(Dificultad, on_delete=models.CASCADE)
    def __str__(self) :
        return self.titulo
    
class Actividad(models.Model):
    nombre = models.CharField(max_length=500)
    fechaInicio = models.DateField('Fecha de inicio')
    fechaFin = models.DateField('Fecha de fin')
    duracion = models.DurationField()
    def __str__(self) :
        return self.nombre

class Uf(models.Model):
    siglas = models.CharField(max_length=100)
    nombre = models.CharField(max_length=256)
    def __str__(self) :
        return self.siglas

class Grupo(models.Model):
    nombre = models.CharField(max_length=500)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    cupo = models.IntegerField()
    estado = models.BooleanField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    def __str__(self) :
        return self.nombre + '.' + str(self.uf)
    
class Carrera(models.Model):
    siglas = models.CharField(max_length=3)
    nombre = models.CharField(max_length=100)
    def __str__(self) :
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
    def __str__(self) :
        return self.matricula + ': ' + self.nombre + ' ' + self.apellidoPat

class EstudianteGrupo(models.Model):
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.estudiante) + ' | ' + str(self.grupo)

class ActividadGrupo(models.Model):
    grupo =models.ForeignKey(Grupo,on_delete=models.CASCADE)
    actividad =models.ForeignKey(Actividad,on_delete=models.CASCADE)
    def __str__(self) :
        return super().__str__()
   
class ActividadPregunta(models.Model):
    actividad = models.ForeignKey(Actividad,on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    valor = models.IntegerField(default=1)
    def __str__(self):
        return str(self.actividad)+' '+str(self.pregunta)

class Calificacion(models.Model):
    ponderacion = models.IntegerField(default=0)
    puntosTotal = models.IntegerField("Puntos totales", default=0)
    actividad = models.ForeignKey(ActividadPregunta,on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.ponderacion) + '/' + str(self.puntosTotal)
    