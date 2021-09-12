# Generated by Django 3.2.6 on 2021-09-12 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datauser', '0002_auto_20210911_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='datospersonales',
            options={'verbose_name': 'Datos del Usuario', 'verbose_name_plural': 'Datos Personales'},
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesion_user', models.CharField(max_length=100, verbose_name='Profesión')),
                ('perfil_user', models.TextField(max_length=5000, verbose_name='Perfil Profesional')),
                ('creado_el', models.DateTimeField(auto_now=True, verbose_name='Creado el')),
                ('modificado_el', models.DateTimeField(auto_now_add=True, verbose_name='Modificado el')),
                ('identidy_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='NickName')),
            ],
            options={
                'verbose_name': 'Perfil de Usuario',
                'verbose_name_plural': 'Perfil de Usuario',
            },
        ),
    ]