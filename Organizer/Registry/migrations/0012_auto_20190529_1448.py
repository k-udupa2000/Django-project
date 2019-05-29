# Generated by Django 2.2.1 on 2019-05-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0011_auto_20190528_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=250, verbose_name='User Name')),
                ('password', models.CharField(default='', max_length=100, verbose_name='Password')),
            ],
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('-studentName',)},
        ),
    ]
