# Generated by Django 4.1.3 on 2023-12-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_status_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]