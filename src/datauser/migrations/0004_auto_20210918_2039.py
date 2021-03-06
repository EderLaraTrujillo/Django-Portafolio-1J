# Generated by Django 3.2.6 on 2021-09-19 01:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datauser', '0003_auto_20210912_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datospersonales',
            name='creado_el',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado el'),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='describe_user',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Perfil del Usuario'),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='modificado_el',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado el'),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='creado_el',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado el'),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='modificado_el',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado el'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='creado_el',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado el'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='modificado_el',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado el'),
        ),
    ]
