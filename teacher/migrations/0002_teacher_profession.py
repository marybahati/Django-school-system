# Generated by Django 2.2.1 on 2019-05-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='profession',
            field=models.CharField(max_length=90, null=True),
        ),
    ]