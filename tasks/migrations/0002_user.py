# Generated by Django 5.1.2 on 2024-11-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]