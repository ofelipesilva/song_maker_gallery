# Generated by Django 3.0.6 on 2020-05-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_admin', '0014_auto_20200522_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.TextField(),
        ),
    ]
