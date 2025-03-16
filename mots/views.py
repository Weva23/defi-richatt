from rest_framework import viewsets, permissions
from .models import Utilisateur, Mot, Definition, Contribution, Validation
from .serializers import UtilisateurSerializer, MotSerializer, DefinitionSerializer, ContributionSerializer, ValidationSerializer

from .serializers import UtilisateurSerializer, MotSerializer, DefinitionSerializer, ContributionSerializer, ValidationSerializer
from .permissions import IsModeratorOrReadOnly, IsAdminOrReadOnly  # Ajoute cette ligne

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAuthenticated]

class MotViewSet(viewsets.ModelViewSet):
    queryset = Mot.objects.all()
    serializer_class = MotSerializer

class DefinitionViewSet(viewsets.ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

class ValidationViewSet(viewsets.ModelViewSet):
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    
    
    
class MotViewSet(viewsets.ModelViewSet):
    queryset = Mot.objects.all()
    serializer_class = MotSerializer
    permission_classes = [IsModeratorOrReadOnly]

class ValidationViewSet(viewsets.ModelViewSet):
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    permission_classes = [IsAdminOrReadOnly]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mot

@api_view(['POST'])
def enrichir_mot(request):
    mot_id = request.data.get('mot_id')
    if not mot_id:
        return Response({"error": "mot_id est requis"}, status=400)

    try:
        mot = Mot.objects.get(id=mot_id)
        mot.definition += " (Définition enrichie par IA)"
        mot.save(update_fields=['definition'])
        return Response({"message": "Mot enrichi avec succès", "mot": mot.definition})
    except Mot.DoesNotExist:
        return Response({"error": "Mot non trouvé"}, status=404)
