# Generated by Django 5.0.7 on 2024-07-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='items',
            field=models.CharField(max_length=100),
        ),
    ]