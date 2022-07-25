# Generated by Django 4.0.5 on 2022-07-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_work_type_work_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('finish_date', models.DateField(verbose_name='Дата окончания')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description_project', models.TextField(blank=True, max_length=150, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'db_table': 'projects',
            },
        ),
    ]