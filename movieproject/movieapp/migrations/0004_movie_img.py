# Generated by Django 4.0.3 on 2022-03-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_movie_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='no image', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
