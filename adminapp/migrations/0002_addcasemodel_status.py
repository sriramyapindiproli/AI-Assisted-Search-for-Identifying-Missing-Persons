# Generated by Django 4.1.5 on 2023-01-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcasemodel',
            name='status',
            field=models.CharField(default='Not Found', max_length=50),
        ),
    ]
