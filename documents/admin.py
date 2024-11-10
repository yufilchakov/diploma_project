from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from documents.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = ['user', 'file', 'is_approved', 'is_rejected']
    actions = ['approve_documents', 'reject_documents']

    def approve_documents(self, request, queryset):
        """Утверждает выбранные документы, устанавливая их статус как одобренный."""
        for document in queryset:
            document.is_approved = True
            document.is_rejected = False
            document.save()
            send_mail(
                'Документ одобрен',
                'Ваш документ одобрен.',
                settings.EMAIL_HOST_USER,
                [document.user.email],
                fail_silently=False,
            )
        self.message_user(request, f'{queryset.count()} документа(ов) одобрены.')

    approve_documents.short_description = 'Утвердить выбранные документы'

    def reject_documents(self, request, queryset):
        """Отклоняет выбранные документы, устанавливая их статус как отклоненный."""
        for document in queryset:
            document.is_rejected = True
            document.is_approved = False
            document.save()
            send_mail(
                'Документ отклонен',
                'Ваш документ отклонен.',
                settings.EMAIL_HOST_USER,
                [document.user.email],
                fail_silently=False,
            )
        self.message_user(request, f'{queryset.count()} документа(ов) отклонены.')

    reject_documents.short_description = 'Отклонить выбранные документы'
