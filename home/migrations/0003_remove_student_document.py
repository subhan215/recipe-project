# Generated by Django 5.0.1 on 2024-01-11 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='document',
        ),
    ]
