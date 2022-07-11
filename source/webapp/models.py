from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Status(BaseModel):
    status = models.CharField(max_length=100, null=True, blank=True, verbose_name="Статус")

    def __str__(self):
        return f"{self.status}"

    class Meta:
        db_table = "statuses"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Type(BaseModel):
    type = models.CharField(max_length=100, null=True, blank=True, verbose_name="Тип")

    def __str__(self):
        return f"{self.type}"

    class Meta:
        db_table = "types"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Work(BaseModel):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=100, null=True, blank=True, verbose_name="Описание")
    status = models.ForeignKey("webapp.Status", on_delete=models.CASCADE, related_name="Statuses",
                               verbose_name="Статус")
    types = models.ManyToManyField("webapp.Type", related_name="works", blank=True)

    def __str__(self):
        return f"{self.pk}. {self.description} - {self.status} - {self.summary} - {self.type}"

    class Meta:
        db_table = "works"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

# Create your models here.
