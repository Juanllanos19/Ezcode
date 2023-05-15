from django.urls import path
from rest_framework import routers
from .views import DepartamentoViewSet, ProfesorViewSet, PeriodoViewSet, TemaViewSet, DificultadViewSet, PreguntaViewSet, ActividadViewSet, UfViewSet, GrupoViewSet, CarreraViewSet, EstudianteViewSet, EstudianteGrupoViewSet, ActividadGrupoViewSet, ActividadPreguntaViewSet, CalificacionViewSet

router = routers.DefaultRouter()
router.register('departamento',DepartamentoViewSet)
router.register('profesor',ProfesorViewSet)
router.register('periodo',PeriodoViewSet)
router.register('tema',TemaViewSet)
router.register('dificultad',DificultadViewSet)
router.register('pregunta',PreguntaViewSet)
router.register('actividad',ActividadViewSet)
router.register('uf',UfViewSet)
router.register('grupo',GrupoViewSet)
router.register('carrera',CarreraViewSet)
router.register('estudiante',EstudianteViewSet)
router.register('estudianteGrupo',EstudianteGrupoViewSet)
router.register('actividaGrupo',ActividadGrupoViewSet)
router.register('actividaPregunta',ActividadPreguntaViewSet)
router.register('calificacion',CalificacionViewSet)
urlpatterns = router.urls