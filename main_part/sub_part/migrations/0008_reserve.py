# Generated by Django 3.2.3 on 2021-06-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0007_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('datefrom', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('dateto', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('deposit', models.CharField(max_length=100)),
                ('deliver', models.CharField(max_length=100)),
                ('tax', models.CharField(max_length=100)),
                ('collect', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
        ),
    ]