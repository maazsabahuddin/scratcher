# Generated by Django 5.0 on 2023-12-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('experience', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
