# Generated by Django 2.1.7 on 2019-05-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_stations', '0008_auto_20190526_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ImageField(upload_to='static/img/', width_field=100),
        ),
    ]
