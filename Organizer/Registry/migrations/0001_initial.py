# Generated by Django 2.1.5 on 2019-05-28 07:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=250)),
                ('phone1', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be of the form: 9876543210.', regex='^\\+?1?\\d{9, 10}$')])),
                ('phone2', models.CharField(default='', max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be of the form: 9876543210.', regex='^\\+?1?\\d{9, 10}$')])),
                ('lastFeesPaid', models.DateTimeField(auto_now_add=True)),
                ('lastAttended', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('studentName', 'Student Name'), ('phone1', 'Primary Phone No.'), ('phone2', 'Secondary Phone No.'), ('lastFeesPaid', 'Last Fees Paid'), ('lastAttended', 'Last Class Attended')], default='draft', max_length=20)),
            ],
        ),
    ]
