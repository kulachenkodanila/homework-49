# Generated by Django 4.0.5 on 2022-08-14 18:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0012_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]