# Generated by Django 2.2.1 on 2019-05-31 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0017_auto_20190530_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedata',
            name='no_of_class_attended',
            field=models.IntegerField(default=0),
        ),
    ]