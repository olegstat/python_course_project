# Generated by Django 3.0.2 on 2020-02-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200129_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbase',
            name='engine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carbase',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='carbase',
            name='year',
            field=models.IntegerField(),
        ),
    ]
