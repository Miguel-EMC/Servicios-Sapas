# Generated by Django 4.2.7 on 2023-11-21 02:00

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spa_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('thumbnail', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255, null=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
        ),
    ]
