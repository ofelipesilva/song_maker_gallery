# Generated by Django 3.0.6 on 2020-05-22 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_admin', '0016_auto_20200522_1747'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='gallery',
            name='Unique Gallery',
        ),
    ]