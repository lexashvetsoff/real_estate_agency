# Generated by Django 2.2.24 on 2022-04-27 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20220423_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_complaint', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]