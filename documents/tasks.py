from celery import shared_task
from django.core.mail import send_mail

from config import settings
from documents.models import Document


@shared_task
def notify_admin(document_id):
    """Отправляет уведомление администратору о новом документе."""
    document = Document.objects.get(id=document_id)
    send_mail(
        'Новый документ загружен',
        f'Новый документ был загружен пользователем {document.user}.',
        settings.DEFAULT_FROM_EMAIL,
        settings.ADMIN_EMAIL,
        fail_silently=False,
        )
