# Generated by Django 4.1.4 on 2023-01-06 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('address', '0001_initial'),
        ('campus', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=30)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
                ('campus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='campus.campus')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor', to='department.department')),
                ('students', models.ManyToManyField(related_name='professor', to='student.students')),
            ],
            options={
                'db_table': 'professor',
            },
        ),
    ]
