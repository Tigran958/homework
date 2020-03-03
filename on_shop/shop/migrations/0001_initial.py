# Generated by Django 2.2.7 on 2019-12-01 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=100)),
                ('ptype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.PType')),
            ],
        ),
    ]