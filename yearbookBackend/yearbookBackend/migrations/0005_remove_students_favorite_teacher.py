# Generated by Django 5.2.1 on 2025-05-29 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbookBackend', '0004_students_favorite_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='favorite_teacher',
        ),
    ]
