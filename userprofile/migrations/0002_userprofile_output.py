# Generated by Django 4.2.3 on 2024-02-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='output',
            field=models.CharField(blank=True, null=True),
        ),
    ]
