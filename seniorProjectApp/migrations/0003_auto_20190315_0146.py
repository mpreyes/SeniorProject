# Generated by Django 2.0.2 on 2019-03-15 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seniorProjectApp', '0002_auto_20190315_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='linksID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]