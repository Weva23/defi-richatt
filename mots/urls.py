from django.urls import path, include
from .views import enrichir_mot

from rest_framework.routers import DefaultRouter
from .views import UtilisateurViewSet, MotViewSet, DefinitionViewSet, ContributionViewSet, ValidationViewSet, enrichir_mot  # Ajoute enrichir_mot ici !

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'mots', MotViewSet)
router.register(r'definitions', DefinitionViewSet)
router.register(r'contributions', ContributionViewSet)
router.register(r'validations', ValidationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('enrichir-mot/', enrichir_mot, name="enrichir-mot"),
]
