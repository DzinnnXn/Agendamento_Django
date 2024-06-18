# Generated by Django 5.0.6 on 2024-06-09 23:53

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agendamento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salas', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=50)),
                ('equipamentos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('idade', models.IntegerField()),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('quartos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Agendamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias', models.DateField(default=datetime.datetime.now)),
                ('periodo', models.CharField(choices=[('manhaA', 'Manhã A'), ('manhaB', 'Manhã B'), ('tardeA', 'Tarde A'), ('tardeB', 'Tarde B'), ('noiteA', 'Noite A')], max_length=10)),
                ('agendado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agendamento.salas')),
            ],
            options={
                'unique_together': {('sala', 'dias', 'periodo')},
            },
        ),
    ]
