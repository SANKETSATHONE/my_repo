# Generated by Django 4.1.4 on 2023-04-14 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='quantity',
            new_name='qty',
        ),
    ]