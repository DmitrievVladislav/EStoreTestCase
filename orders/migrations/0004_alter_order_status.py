# Generated by Django 4.2.6 on 2023-10-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_products_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(default='В обработке', max_length=256),
        ),
    ]
