# Generated by Django 2.1.7 on 2019-05-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_stations', '0003_auto_20190526_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fact',
            old_name='description',
            new_name='short_description',
        ),
        migrations.AddField(
            model_name='fact',
            name='main_text',
            field=models.TextField(default='main_text'),
            preserve_default=False,
        ),
    ]
