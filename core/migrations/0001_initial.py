# Generated by Django 4.2.5 on 2024-05-22 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Отделение',
                'verbose_name_plural': 'Отделения',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(db_index=True, max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('gender', models.IntegerField(choices=[], verbose_name='Пол')),
                ('dc', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('dm', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='workers', to='core.department', verbose_name='Отделение')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
