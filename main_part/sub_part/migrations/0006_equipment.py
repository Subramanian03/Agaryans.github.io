# Generated by Django 3.2.3 on 2021-06-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0005_adminreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('count', models.CharField(max_length=100)),
            ],
        ),
    ]