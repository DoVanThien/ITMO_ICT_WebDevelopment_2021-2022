# Generated by Django 3.2.8 on 2021-10-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_alter_driver_license_kind'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Possection',
            new_name='Possession',
        ),
        migrations.AddField(
            model_name='car',
            name='member',
            field=models.ManyToManyField(through='project_first_app.Possession', to='project_first_app.Owner'),
        ),
    ]
