# Generated by Django 4.1.3 on 2023-06-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_order_adress_order_date_added_order_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photot',
            field=models.ImageField(upload_to='media'),
        ),
    ]
