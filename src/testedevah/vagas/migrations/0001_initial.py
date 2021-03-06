# Generated by Django 2.2.17 on 2020-11-20 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0002_auto_20201120_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.TextField(blank=True, max_length=250)),
                ('duracao_meses', models.IntegerField(blank=True)),
                ('atribuicoes', models.TextField(blank=True, max_length=250)),
                ('nome_cargo', models.TextField(blank=True, max_length=250)),
                ('usuarios_cadastrados', models.ManyToManyField(to='pessoas.Pessoa')),
            ],
        ),
    ]
