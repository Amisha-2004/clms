# Generated by Django 5.1.3 on 2024-11-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('Supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Code', models.CharField(max_length=50, unique=True)),
                ('Address', models.TextField()),
                ('Contact_no', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
