# Generated by Django 4.1.4 on 2024-12-04 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_created=True)),
                ('mavzu', models.CharField(max_length=150)),
                ('nomer', models.CharField(max_length=15)),
                ('muddat', models.DateField()),
                ('javobgar', models.CharField(max_length=20)),
                ('topshiriq_turi', models.CharField(max_length=20)),
                ('topshiriq_kimdan', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('natijasi', models.CharField(max_length=200)),
            ],
        ),
    ]
