# Generated by Django 4.2.3 on 2024-06-07 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('room_level', models.IntegerField(blank=True, default=1)),
                ('city', models.CharField(choices=[('Diana', 'Diana'), ('Sava', 'Sava'), ('Itasy', 'Itasy'), ('Analamanga', 'Analamanga'), ('Vakinankaratra', 'Vakinankaratra'), ('Bongolava', 'Bongolava'), ('Sofia', 'Sofia'), ('Boeny', 'Boeny'), ('Betsiboka', 'Betsiboka'), ('Melaky', 'Melaky'), ('Alaotra-Mangoro', 'Alaotra-Mangoro'), ('Atsinanana', 'Atsinanana'), ('Analanjirofo', 'Analanjirofo'), ("Amoron'i Mania", "Amoron'i Mania"), ('Vatovavy', 'Vatovavy'), ('Haute Matsiatra', 'Haute Matsiatra'), ('Fitovinany', 'Fitovinany'), ('Atsimo-Atsinanana', 'Atsimo-Atsinanana'), ('Ihorombe', 'Ihorombe'), ('Menabe', 'Menabe'), ('Atsimo-Andrefana', 'Atsimo-Andrefana'), ('Androy', 'Androy'), ('Anôsy', 'Anôsy')], max_length=100)),
                ('last_flag_found', models.DateTimeField(blank=True, null=True)),
                ('current_flag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ctf.flag')),
                ('flag_found', models.ManyToManyField(blank=True, related_name='flag_found', to='ctf.flag')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.flag')),
            ],
        ),
    ]
