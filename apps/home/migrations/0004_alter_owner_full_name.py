# Generated by Django 3.2.16 on 2022-11-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(blank=True, max_length=70, unique=True),
        ),
    ]
