# Generated by Django 4.2.6 on 2023-10-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerss', '0005_alter_offer_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='vendor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='vendor_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
