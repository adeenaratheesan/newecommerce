# Generated by Django 4.1.7 on 2023-02-16 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('ph_number', models.CharField(max_length=20)),
                ('e_mail', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=16)),
                ('image', models.ImageField(upload_to='customer/')),
            ],
        ),
    ]
