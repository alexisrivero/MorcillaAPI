# Generated by Django 3.0.7 on 2020-10-20 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cocinero',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('nacionalidad', models.ForeignKey(blank=True, null=True,
                                                   on_delete=django.db.models.deletion.DO_NOTHING, to='prueba.Pais')),
                ('pizzas', models.ManyToManyField(to='prueba.Pizza')),
            ],
        ),
    ]