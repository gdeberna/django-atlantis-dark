# Generated by Django 3.2.16 on 2022-11-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_tool_rto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
