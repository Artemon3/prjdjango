# Generated by Django 3.2.12 on 2024-01-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='опубликован'),
        ),
    ]
