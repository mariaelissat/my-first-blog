# Generated by Django 3.2.25 on 2024-04-06 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='autora',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='entrada',
            old_name='texto',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='entrada',
            old_name='titulo',
            new_name='title',
        ),
    ]
