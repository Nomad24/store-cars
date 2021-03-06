# Generated by Django 3.0.8 on 2020-07-18 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200718_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='store.Category'),
        ),
        migrations.AlterField(
            model_name='car',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='cars', to='store.Tag'),
        ),
    ]
