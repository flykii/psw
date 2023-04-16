# Generated by Django 4.2 on 2023-04-12 20:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0002_rename_carga_horario_evento_carga_horaria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.ManyToManyField(null=True, related_name='evento_participante', to=settings.AUTH_USER_MODEL),
        ),
    ]