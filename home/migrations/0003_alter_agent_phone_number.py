# Generated by Django 4.0.3 on 2022-03-23 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_agent_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
