# Generated by Django 3.0.4 on 2020-03-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='first name')),
                ('lname', models.CharField(max_length=50, verbose_name='last name')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
                ('gender', models.CharField(max_length=50, verbose_name='gender')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True, verbose_name='email')),
                ('phone', models.CharField(max_length=50, unique=True, verbose_name='phone number')),
            ],
        ),
    ]
