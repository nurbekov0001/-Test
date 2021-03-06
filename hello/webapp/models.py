from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Book(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="имя автора ")
    email = models.EmailField(null=False, blank=False, verbose_name="почта автора")
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name="текст записи")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=False, blank=False, default="active",
                              verbose_name="Статус задачи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книгии'

    def __str__(self):
        return f'{self.id}. {self.name}:{self.email} {self.description} {self.status}{self.created_at}{self.updated_at}'
# Create your models here.
