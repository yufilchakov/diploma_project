from unittest.mock import patch
from django.urls import reverse

from django.test import TestCase, RequestFactory
from rest_framework.test import APIClient
from urllib.parse import urljoin

from documents.tasks import notify_admin
from config import settings
from documents.models import Document
from users.models import User


class DocumentsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email=settings.ADMIN_EMAIL, password='123qwe')
        self.document = Document.objects.create(file='path/to/file', user=self.user, is_approved=False,
                                                is_rejected=False)
        self.client = APIClient()
        self.request_factory = RequestFactory()
        self.client.force_authenticate(user=self.user)
    
    def test_document_creation(self):
        """Тестируем создание документа."""
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(self.document.user, self.user)
        self.assertEqual(self.document.is_approved, False)
        self.assertEqual(self.document.is_rejected, False)
        
    def test_document_retrieve(self):
        """Тестируем получение документа."""
        url = reverse('documents:documents_retrieve', args=(self.document.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        expected_url = urljoin('http://testserver', self.document.file.url)
        self.assertEqual(response.data['file'], expected_url)
        self.assertEqual(response.data['user'], self.document.user.id)
        self.assertEqual(response.data['is_approved'], self.document.is_approved)
        self.assertEqual(response.data['is_rejected'], self.document.is_rejected)
        

class NotifyAdminTaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email=settings.ADMIN_EMAIL, password='123qwe')
        self.document = Document.objects.create(file='path/to/file', user=self.user, is_approved=False,
                                                is_rejected=False)
        
    def test_notify_admin(self):
        """Тестируем задачу уведомления администратора."""
        with patch('documents.tasks.send_mail') as send_mail:
            notify_admin(self.document.pk)
            send_mail.assert_called_once_with(
                'Новый документ загружен',
                f'Новый документ был загружен пользователем {self.document.user.email}.',
                settings.DEFAULT_FROM_EMAIL,
                settings.ADMIN_EMAIL,
                fail_silently=False,
            )
