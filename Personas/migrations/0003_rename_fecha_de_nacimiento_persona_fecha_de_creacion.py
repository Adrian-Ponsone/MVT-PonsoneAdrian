# Generated by Django 4.1.1 on 2022-10-04 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0002_persona_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='fecha_de_nacimiento',
            new_name='fecha_de_creacion',
        ),
    ]
