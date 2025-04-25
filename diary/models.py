from django.db import models

from users.models import User


# Create your models here.
class Note(models.Model):
    title = models.CharField("Название", max_length=100, blank=True, null=True)
    note = models.TextField("Запись")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
