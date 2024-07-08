# Generated by Django 5.0.6 on 2024-07-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasajero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=250)),
                ('fecha_nacimiento', models.DateField()),
                ('documento', models.IntegerField()),
                ('cuidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
