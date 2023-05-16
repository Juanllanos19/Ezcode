from rest_framework.serializers import ModelSerializer, ALL_FIELDS
from .models import Departamento, Profesor, Periodo, Tema, Dificultad, Pregunta, Actividad, Uf, Grupo, Carrera, Estudiante, EstudianteGrupo, ActividadGrupo, ActividadPregunta, Calificacion
#commit de prueba
class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = ALL_FIELDS

class ProfesorSerializer(ModelSerializer):
    class Meta:
        model = Profesor
        fields = ALL_FIELDS

class PeriodoSerializer(ModelSerializer):
    class Meta:
        model = Periodo 
        fields = ALL_FIELDS

class TemaSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = ALL_FIELDS

class DificultadSerializer(ModelSerializer):
    class Meta:
        model = Dificultad
        fields = ALL_FIELDS

class PreguntaSerializer(ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ALL_FIELDS

class ActividadSerializer(ModelSerializer):
    class Meta:
        model = Actividad
        fields = ALL_FIELDS

class UfSerializer(ModelSerializer):
    class Meta:
        model = Uf
        fields = ALL_FIELDS

class GrupoSerializer(ModelSerializer):
    class Meta:
        model = Grupo
        fields = ALL_FIELDS

class CarreraSerializer(ModelSerializer):
    class Meta:
        model = Carrera
        fields = ALL_FIELDS

class EstudianteSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ALL_FIELDS

class EstudianteGrupoSerializer(ModelSerializer):
    class Meta:
        model = EstudianteGrupo
        fields = ALL_FIELDS

class ActividadGrupoSerializer(ModelSerializer):
    class Meta:
        model = ActividadGrupo
        fields = ALL_FIELDS

class ActividadPreguntaSerializer(ModelSerializer):
    class Meta:
        model = ActividadPregunta
        fields = ALL_FIELDS

class CalificacionSerializer(ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ALL_FIELDS