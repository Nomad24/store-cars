# Generated by Django 3.0.8 on 2020-07-18 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200718_0850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Cars'},
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
    ]
