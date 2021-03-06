# Generated by Django 4.0.5 on 2022-06-10 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20, verbose_name='Група документу')),
            ],
        ),
        migrations.CreateModel(
            name='Documentations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Назва документу')),
                ('content', models.TextField(verbose_name='Документ')),
                ('upload_date', models.DateField(auto_now_add=True, verbose_name='Дата публікації')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Дата оновлення')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публікація')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Documentations', to='documents.groups')),
            ],
        ),
    ]
