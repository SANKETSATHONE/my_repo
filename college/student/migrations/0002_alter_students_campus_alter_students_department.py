# Generated by Django 4.1.4 on 2023-01-06 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0002_alter_campus_address'),
        ('department', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='campus.campus'),
        ),
        migrations.AlterField(
            model_name='students',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='department.department'),
        ),
    ]
