# Generated by Django 4.1.4 on 2022-12-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='book name')),
                ('subject', models.CharField(max_length=20, null=True, verbose_name='subject name')),
                ('price', models.FloatField(verbose_name='book price')),
                ('quantity', models.IntegerField(default=1, verbose_name='book quantity')),
                ('purchase_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
