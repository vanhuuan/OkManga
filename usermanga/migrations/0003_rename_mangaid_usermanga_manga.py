# Generated by Django 4.0.4 on 2022-06-09 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanga', '0002_rename_chapterid_usermanga_mangaid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermanga',
            old_name='mangaId',
            new_name='manga',
        ),
    ]
