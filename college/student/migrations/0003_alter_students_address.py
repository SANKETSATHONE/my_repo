# Generated by Django 4.1.4 on 2023-01-06 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('student', '0002_alter_students_campus_alter_students_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='address.address'),
        ),
    ]
