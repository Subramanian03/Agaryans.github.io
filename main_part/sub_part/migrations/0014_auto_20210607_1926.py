# Generated by Django 3.2.3 on 2021-06-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0013_auto_20210607_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='count',
            field=models.CharField(default=23, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='product',
            field=models.CharField(default=23, max_length=100),
            preserve_default=False,
        ),
    ]
