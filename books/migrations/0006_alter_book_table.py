# Generated by Django 5.0.2 on 2025-02-10 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_rename_auther_book_author'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
