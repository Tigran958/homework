# Generated by Django 2.2.7 on 2019-11-14 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='name',
            new_name='agrcode',
        ),
    ]
