# Generated by Django 2.0.2 on 2019-03-25 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seniorProjectApp', '0004_auto_20190315_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
