# Generated by Django 2.0.3 on 2019-01-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_booklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklist',
            name='location',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddIndex(
            model_name='booklist',
            index=models.Index(fields=['bookname'], name='bookname_idx'),
        ),
    ]
