# Generated by Django 4.0.4 on 2022-06-19 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserManga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manga.manga')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
