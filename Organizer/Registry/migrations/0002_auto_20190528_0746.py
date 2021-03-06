# Generated by Django 2.1.5 on 2019-05-28 07:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='status',
        ),
        migrations.AlterField(
            model_name='master',
            name='phone1',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be of the form: 9876543210.', regex='^[0-9]{10}$')]),
        ),
        migrations.AlterField(
            model_name='master',
            name='phone2',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be of the form: 9876543210.', regex='^[0-9]{10}$')]),
        ),
    ]
