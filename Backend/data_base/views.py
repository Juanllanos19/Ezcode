from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Departamento, Profesor, Periodo, Tema, Dificultad, Pregunta, Actividad, Uf, Grupo, Carrera, Estudiante, EstudianteGrupo, ActividadGrupo, ActividadPregunta, Calificacion
from .serializers import DepartamentoSerializer, ProfesorSerializer, PeriodoSerializer, TemaSerializer, DificultadSerializer, PreguntaSerializer, ActividadSerializer, UfSerializer, GrupoSerializer, CarreraSerializer, EstudianteSerializer, EstudianteGrupoSerializer, ActividadGrupoSerializer, ActividadPreguntaSerializer, CalificacionSerializer

class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class ProfesorViewSet(ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class PeriodoViewSet(ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer

class TemaViewSet(ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class DificultadViewSet(ModelViewSet):
    queryset = Dificultad.objects.all()
    serializer_class = DificultadSerializer

class PreguntaViewSet(ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class ActividadViewSet(ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class UfViewSet(ModelViewSet):
    queryset = Uf.objects.all()
    serializer_class = UfSerializer

class GrupoViewSet(ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class CarreraViewSet(ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class EstudianteViewSet(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteGrupoViewSet(ModelViewSet):
    queryset = EstudianteGrupo.objects.all()
    serializer_class = EstudianteGrupoSerializer

class ActividadGrupoViewSet(ModelViewSet):
    queryset = ActividadGrupo.objects.all()
    serializer_class = ActividadGrupoSerializer

class ActividadPreguntaViewSet(ModelViewSet):
    queryset = ActividadPregunta.objects.all()
    serializer_class = ActividadPreguntaSerializer

class CalificacionViewSet(ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

