# Generated by Django 4.0 on 2021-12-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0009_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
