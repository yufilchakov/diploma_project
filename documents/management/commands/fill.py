from django.core.management.base import BaseCommand
from django.utils import timezone

from documents.models import Document
from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания тестовых документов."""
    def handle(self, *args, **options):
        user1, _ = User.objects.get_or_create(email='user1@example.com')
        user2, _ = User.objects.get_or_create(email='user2@example.com')
        user3, _ = User.objects.get_or_create(email='user3@example.com')
        
        Document.objects.create(
            user=user1,
            file='media/documents/docs/document_1.pdf',
            uploaded_at=timezone.now(),
            is_approved=True,
            is_rejected=False
        )
        
        Document.objects.create(
            user=user2,
            file='media/documents/docs/document_2.docx',
            uploaded_at=timezone.now(),
            is_approved=False,
            is_rejected=True
        )
        
        Document.objects.create(
            user=user3,
            file='media/documents/docs/document_3.txt',
            uploaded_at=timezone.now(),
            is_approved=False,
            is_rejected=False
        )
