# Generated by Django 2.2.17 on 2020-11-20 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaga',
            old_name='atribuicoes',
            new_name='beneficios',
        ),
        migrations.RenameField(
            model_name='vaga',
            old_name='nome_cargo',
            new_name='descricao',
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='duracao_meses',
        ),
        migrations.AddField(
            model_name='vaga',
            name='nome_vaga',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='vaga',
            name='requisitos',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='vaga',
            name='salario',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='vaga',
            name='tipo_vaga',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='nome_empresa',
            field=models.IntegerField(blank=True),
        ),
    ]