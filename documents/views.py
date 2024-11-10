from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from documents.models import Document
from documents.serializer import DocumentSerializer
from documents.tasks import notify_admin


class DocumentUploadView(generics.CreateAPIView):
    """Загрузка документа."""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Сохраняем документ и отправляем уведомление администратору."""
        document = serializer.save(user=self.request.user)
        notify_admin.delay(document.id)

       
class DocumentRetrieveAPIView(generics.RetrieveAPIView):
    """Информация о документе."""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
