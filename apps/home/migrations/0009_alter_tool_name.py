# Generated by Django 3.2.16 on 2022-11-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_tool_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
