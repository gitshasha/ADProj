# Generated by Django 4.1.1 on 2023-01-05 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fruit', '0003_delete_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_Main_Img',
            new_name='Main_Img',
        ),
    ]