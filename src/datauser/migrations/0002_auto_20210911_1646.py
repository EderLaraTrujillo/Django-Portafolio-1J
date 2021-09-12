# Generated by Django 3.2.6 on 2021-09-11 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datauser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datospersonales',
            name='creado_el',
            field=models.DateTimeField(auto_now=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='datospersonales',
            name='modificado_el',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Modificado el'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='identidy_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='NickName'),
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_habilidad', models.CharField(max_length=100, verbose_name='Habilidad')),
                ('porcen_habilidad', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Porcentaje de Habilidad')),
                ('status_habilidad', models.BooleanField(default=True, verbose_name='Estado de Habilidad')),
                ('creado_el', models.DateTimeField(auto_now=True, verbose_name='Creado el')),
                ('modificado_el', models.DateTimeField(auto_now_add=True, verbose_name='Modificado el')),
                ('identidy_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='NickName')),
            ],
            options={
                'verbose_name': 'Habilidad del Usuario',
                'verbose_name_plural': 'Habilidades del Usuario',
            },
        ),
    ]