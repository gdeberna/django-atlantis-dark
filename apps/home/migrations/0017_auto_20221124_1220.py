# Generated by Django 3.2.16 on 2022-11-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20221124_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='implementation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='risk',
            field=models.CharField(default='To be calculated', max_length=50),
        ),
    ]
