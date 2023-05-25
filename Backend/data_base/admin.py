from django.contrib import admin
from .models import Departamento, Profesor, Periodo, Tema, Pregunta, Dificultad, Actividad, Grupo, Carrera, Estudiante, Calificacion, Uf, EstudianteGrupo, ActividadGrupo, ActividadPregunta
# Register your models here.
admin.site.register(Departamento)
admin.site.register(Profesor)
admin.site.register(Periodo)
admin.site.register(Tema)
admin.site.register(Pregunta)
admin.site.register(Dificultad)
admin.site.register(Actividad)
admin.site.register(Grupo)
admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Calificacion)
admin.site.register(Uf)
admin.site.register(EstudianteGrupo)
admin.site.register(ActividadGrupo)
admin.site.register(ActividadPregunta)