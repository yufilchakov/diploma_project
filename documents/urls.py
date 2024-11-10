from django.urls import path

from documents.apps import DocumentsConfig
from documents.views import DocumentUploadView, DocumentRetrieveAPIView

app_name = DocumentsConfig.name

urlpatterns = [
    path('documents/', DocumentUploadView.as_view(), name='documents'),
    path('documents/<int:pk>/', DocumentRetrieveAPIView.as_view(), name='documents_retrieve')
]