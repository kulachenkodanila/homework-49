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
    projects = models.ForeignKey("webapp.Project", on_delete=models.CASCADE, default=1, related_name="Projects",
                               verbose_name="Проект")

    def __str__(self):
        return f"{self.pk}. {self.description} - {self.status} - {self.summary} - {self.types}"

    class Meta:
        db_table = "works"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

class Project(models.Model):
    start_date = models.DateField(verbose_name="Дата начала")
    finish_date = models.DateField(verbose_name="Дата окончания")
    name = models.CharField(max_length=30, verbose_name="Название")
    description_project = models.TextField(max_length=150, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.pk}. {self.start_date} - {self.finish_date} - {self.name} - {self.description_project}"

    class Meta:
        db_table = "projects"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

# Create your models here.
