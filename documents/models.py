from django.db import models

from users.models import User


class Document(models.Model):
    """Модель документов."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    file = models.FileField(
        upload_to='documents/docs',
        verbose_name='Файл'
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата загрузки'
    )
    is_approved = models.BooleanField(
        default=False,
        verbose_name='Одобрено'
    )
    is_rejected = models.BooleanField(
        default=False,
        verbose_name='Отклонено'
    )

    def __str__(self):
        return f"{self.user} - {self.file.name}"
