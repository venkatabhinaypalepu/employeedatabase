# Generated by Django 4.2.17 on 2024-12-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images')),
                ('designation', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
    ]
