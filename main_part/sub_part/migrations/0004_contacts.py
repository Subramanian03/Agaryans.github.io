# Generated by Django 3.2.3 on 2021-06-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0003_rename_email_id_reg_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]
