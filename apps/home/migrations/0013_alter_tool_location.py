# Generated by Django 3.2.16 on 2022-11-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_tool_enduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
