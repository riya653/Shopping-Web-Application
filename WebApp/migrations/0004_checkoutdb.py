# Generated by Django 5.1.4 on 2025-02-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Place', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile_Number', models.IntegerField(blank=True, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('Pincode', models.IntegerField(blank=True, null=True)),
                ('Total_Price', models.IntegerField(blank=True, null=True)),
                ('Message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
