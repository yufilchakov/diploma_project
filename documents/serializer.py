from rest_framework import serializers
from documents.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """Реализация сериализатора для документов."""
    class Meta:
        model = Document
        fields = '__all__'
