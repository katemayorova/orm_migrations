# Generated by Django 4.0.6 on 2022-07-23 18:56

from django.db import migrations
from school.models import Student


def make_many_teacher(apps, schema_editor):
    for student in Student.objects.all():
        student.teachers.add(student.teacher)


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_student_teachers'),
    ]

    operations = [
        migrations.RunPython(make_many_teacher)
    ]
