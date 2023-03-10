# Generated by Django 4.0.6 on 2023-01-05 10:01

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
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('place', models.IntegerField(choices=[(1, 'Toshkent'), (2, 'Andijon'), (3, "Farg'ona"), (4, 'Namangan'), (5, 'Sirdaryo'), (6, 'Jizzax'), (7, 'Samarqand'), (8, 'Navoiy'), (9, 'Surxondaryo'), (10, 'Qashqadaryo'), (11, 'Xorazm'), (12, 'Qoraqalpoq')], default=1)),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
