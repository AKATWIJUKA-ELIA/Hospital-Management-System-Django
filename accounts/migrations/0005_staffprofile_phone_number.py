# Generated by Django 3.1.7 on 2021-03-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210326_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
