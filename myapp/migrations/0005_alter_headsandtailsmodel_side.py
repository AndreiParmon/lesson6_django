# Generated by Django 5.0.2 on 2024-03-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_headsandtailsmodel_side'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headsandtailsmodel',
            name='side',
            field=models.CharField(default='heads', max_length=10),
        ),
    ]
