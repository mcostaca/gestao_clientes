# Generated by Django 5.0.1 on 2024-01-07 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('date_updated', models.DateField(auto_now=True)),
                ('get_sex', models.CharField(choices=[('MALE', 'M'), ('FEMALE', 'F')], max_length=6)),
            ],
        ),
    ]