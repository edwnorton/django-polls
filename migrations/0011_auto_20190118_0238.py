# Generated by Django 2.0.3 on 2019-01-18 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_booklist_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='location',
            field=models.CharField(default='', max_length=4),
        ),
    ]