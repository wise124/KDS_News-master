# Generated by Django 3.1.3 on 2020-11-23 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_pic',
            field=models.ImageField(default='images/rename.jpg', upload_to='images/'),
        ),
    ]
