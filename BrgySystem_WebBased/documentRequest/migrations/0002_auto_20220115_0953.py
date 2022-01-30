# Generated by Django 3.0.3 on 2022-01-15 01:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documentRequest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docrequest',
            name='DocumentStatus',
        ),
        migrations.CreateModel(
            name='docRequestDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Document_Type', models.CharField(choices=[('Barangay Indigency', 'Barangay Indigency'), ('Barangay Clearance', 'Barangay Clearance'), ('Barangay Residency', 'Barangay Residency')], max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('approved_at', models.DateField(default=datetime.date.today)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
