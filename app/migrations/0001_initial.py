# Generated by Django 4.0.1 on 2022-01-20 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=500, verbose_name='Identificação')),
            ],
            options={
                'verbose_name': 'Alojamento',
                'verbose_name_plural': 'Alojamentos',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Nome')),
                ('brand', models.ImageField(upload_to=None, verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Shed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=500, verbose_name='Identificação')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Galpão',
                'verbose_name_plural': 'Galpões',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=500, verbose_name='Identificação')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.accommodation', verbose_name='Alojamento')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.AddField(
            model_name='accommodation',
            name='shed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.shed', verbose_name='Galpão'),
        ),
    ]
