# Generated by Django 2.2.1 on 2019-05-31 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0018_auto_20190531_0421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storedata',
            old_name='studentname',
            new_name='username',
        ),
    ]
