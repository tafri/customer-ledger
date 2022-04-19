# Generated by Django 4.0.4 on 2022-04-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=8, default=0.0, max_digits=20)),
            ],
        ),
    ]
