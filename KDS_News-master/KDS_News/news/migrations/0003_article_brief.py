# Generated by Django 3.1.3 on 2020-11-17 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201117_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Brief',
            field=models.TextField(default='boom', max_length=400),
            preserve_default=False,
        ),
    ]
