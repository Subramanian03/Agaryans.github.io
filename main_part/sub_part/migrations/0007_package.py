# Generated by Django 3.2.3 on 2021-06-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0006_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('items', models.CharField(max_length=100)),
            ],
        ),
    ]