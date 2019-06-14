# Generated by Django 2.1.7 on 2019-06-14 04:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SpaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spauser',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]