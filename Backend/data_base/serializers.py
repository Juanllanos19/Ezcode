from rest_framework.serializers import ModelSerializer, ALL_FIELDS
from rest_framework import serializers
from .models import Departamento, Profesor, Periodo, Tema, Dificultad, Pregunta, Actividad, Uf, Grupo, Carrera, Estudiante, EstudianteGrupo, ActividadGrupo, ActividadPregunta, Calificacion
class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = ALL_FIELDS

class ProfesorSerializer(ModelSerializer):
    class Meta:
        model = Profesor
        fields = ALL_FIELDS

class ProfesorGetSerializer(ModelSerializer):
    departamento = DepartamentoSerializer()
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

class PreguntaGetSerializer(ModelSerializer):
    tema = TemaSerializer()
    profesor =ProfesorSerializer()
    dificultad = DificultadSerializer()
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

class GrupoGetSerializer(ModelSerializer):
    uf = UfSerializer()
    profesor = ProfesorSerializer()
    periodo = PeriodoSerializer()
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

class EstudianteGetSerializer(ModelSerializer):
    carrera = CarreraSerializer()
    class Meta:
        model = Estudiante
        fields = ALL_FIELDS

class EstudianteGrupoSerializer(ModelSerializer):
    class Meta:
        model = EstudianteGrupo
        fields = ALL_FIELDS


class EstudianteGrupoGetSerializer(ModelSerializer):
    estudiante = EstudianteSerializer()
    grupo = GrupoSerializer()
    class Meta:
        model = EstudianteGrupo
        fields = ALL_FIELDS

class ActividadGrupoSerializer(ModelSerializer):
    class Meta:
        model = ActividadGrupo
        fields = ALL_FIELDS


class ActividadGrupoGetSerializer(ModelSerializer):
    grupo = GrupoSerializer()
    actividad = ActividadSerializer()
    class Meta:
        model = ActividadGrupo
        fields = ALL_FIELDS

class ActividadPreguntaSerializer(ModelSerializer):
    class Meta:
        model = ActividadPregunta
        fields = ALL_FIELDS


class ActividadPreguntaGetSerializer(ModelSerializer):
    actividad = ActividadSerializer()
    pregunta = PreguntaSerializer()
    class Meta:
        model = ActividadPregunta
        fields = ALL_FIELDS

class CalificacionSerializer(ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ALL_FIELDS

class CalificacionGetSerializer(ModelSerializer):
    actividad = ActividadPreguntaSerializer()
    estudiante = EstudianteSerializer()
    class Meta:
        model = Calificacion
        fields = ALL_FIELDS