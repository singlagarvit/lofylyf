# Generated by Django 3.2.3 on 2021-05-16 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_query_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='query',
            options={'ordering': ('-received_on',), 'verbose_name_plural': 'Queries'},
        ),
    ]
