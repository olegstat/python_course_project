# Generated by Django 3.0.2 on 2020-01-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200129_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbase',
            name='ad_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carbase',
            name='ad_url',
            field=models.URLField(),
        ),
    ]
