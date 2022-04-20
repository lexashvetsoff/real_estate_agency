# Generated by Django 2.2.24 on 2022-04-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20220419_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.AddField(
            model_name='flat',
            name='owner',
            field=models.ManyToManyField(related_name='owner_deprecated', to='property.Owner', verbose_name='Владелец'),
        ),
    ]
