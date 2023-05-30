from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Departamento, Profesor, Periodo, Tema, Dificultad, Pregunta, Actividad, Uf, Grupo, Carrera, Estudiante, EstudianteGrupo, ActividadGrupo, ActividadPregunta, Calificacion
from .serializers import DepartamentoSerializer, ProfesorSerializer, ProfesorGetSerializer, PeriodoSerializer, TemaSerializer, DificultadSerializer, PreguntaSerializer, PreguntaGetSerializer
from .serializers import ActividadSerializer, UfSerializer, GrupoSerializer, GrupoGetSerializer, CarreraSerializer, EstudianteSerializer, EstudianteGetSerializer, EstudianteGrupoSerializer
from .serializers import EstudianteGrupoGetSerializer, ActividadGrupoSerializer, ActividadGrupoGetSerializer, ActividadPreguntaSerializer, ActividadPreguntaGetSerializer, CalificacionSerializer, CalificacionGetSerializer

class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()
    defserializer_class = DepartamentoSerializer

class ProfesorViewSet(ModelViewSet):
    queryset = Profesor.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProfesorGetSerializer
        return ProfesorSerializer

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
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return PreguntaGetSerializer
        return PreguntaSerializer

class ActividadViewSet(ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class UfViewSet(ModelViewSet):
    queryset = Uf.objects.all()
    serializer_class = UfSerializer

class GrupoViewSet(ModelViewSet):
    queryset = Grupo.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return GrupoGetSerializer
        return GrupoSerializer

class CarreraViewSet(ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class EstudianteViewSet(ModelViewSet):
    queryset = Estudiante.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return EstudianteGetSerializer
        return EstudianteSerializer

class EstudianteGrupoViewSet(ModelViewSet):
    queryset = EstudianteGrupo.objects.all()
    def get_serializer_class(self): 
        if self.request.method in ['GET']:
            return EstudianteGrupoGetSerializer
        return EstudianteGrupoSerializer

class ActividadGrupoViewSet(ModelViewSet):
    queryset = ActividadGrupo.objects.all()
    def get_serializer_class(self): 
        if self.request.method in ['GET']:
            return ActividadGrupoGetSerializer
        return ActividadGrupoSerializer

class ActividadPreguntaViewSet(ModelViewSet):
    queryset = ActividadPregunta.objects.all()
    def get_serializer_class(self): 
        if self.request.method in ['GET']:        
            return ActividadPreguntaGetSerializer
        return ActividadPreguntaSerializer

class CalificacionViewSet(ModelViewSet):
    queryset = Calificacion.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return CalificacionGetSerializer
        return CalificacionSerializer

