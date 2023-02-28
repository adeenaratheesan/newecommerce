# Generated by Django 4.1.7 on 2023-02-18 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homecommon', '0002_alter_customer_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=20)),
                ('e_mail', models.CharField(max_length=100)),
                ('company_logo', models.ImageField(upload_to='seller/')),
                ('bank_name', models.CharField(max_length=150)),
                ('acc_name', models.CharField(max_length=150)),
                ('accc_no', models.BigIntegerField()),
                ('ifsc', models.CharField(max_length=150)),
                ('branch_name', models.CharField(max_length=500)),
                ('Username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
