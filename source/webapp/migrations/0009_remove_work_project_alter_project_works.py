# Generated by Django 4.0.5 on 2022-07-27 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_work_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='project',
        ),
        migrations.AlterField(
            model_name='project',
            name='works',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='works', to='webapp.work', verbose_name='Задача'),
        ),
    ]