# Generated by Django 3.2.3 on 2021-06-11 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0016_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminreg',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='adminreg',
            name='psw_repeat',
        ),
        migrations.RemoveField(
            model_name='reg',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='reg',
            name='psw_repeat',
        ),
    ]