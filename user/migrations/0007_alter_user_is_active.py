# Generated by Django 4.0.5 on 2022-07-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_profile_address_profile_city_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]