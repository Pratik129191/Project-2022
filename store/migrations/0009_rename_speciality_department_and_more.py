# Generated by Django 4.0.5 on 2022-06-16 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_report_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Speciality',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='speciality',
            new_name='department',
        ),
    ]