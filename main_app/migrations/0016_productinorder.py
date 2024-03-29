# Generated by Django 4.1.3 on 2023-11-08 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_order_session_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=225, null=True)),
                ('product_total_price', models.IntegerField(null=True)),
                ('number', models.PositiveBigIntegerField(null=True)),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_edited', models.DateTimeField(auto_now=True, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.product')),
            ],
        ),
    ]
