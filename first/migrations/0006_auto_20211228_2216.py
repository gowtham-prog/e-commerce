# Generated by Django 3.2.9 on 2021-12-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_comments_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='ImageURL',
        ),
        migrations.AddField(
            model_name='products',
            name='Image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
