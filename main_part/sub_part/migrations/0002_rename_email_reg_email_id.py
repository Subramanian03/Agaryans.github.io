# Generated by Django 3.2.3 on 2021-06-02 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg',
            old_name='email',
            new_name='Email_id',
        ),
    ]
