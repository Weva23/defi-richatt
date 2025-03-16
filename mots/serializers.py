from rest_framework import serializers
from .models import Utilisateur, Mot, Definition, Variante, Validation, Contribution, Commentaire, Recompense, Source, ImportationTexte, Challenge1000Mots

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class MotSerializer(serializers.ModelSerializer):
    definitions = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Mot
        fields = '__all__'

class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = '__all__'

class VarianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variante
        fields = '__all__'

class ValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = '__all__'

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'

class RecompenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recompense
        fields = '__all__'

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class ImportationTexteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportationTexte
        fields = '__all__'

class Challenge1000MotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge1000Mots
        fields = '__all__'
