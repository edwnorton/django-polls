# Generated by Django 2.0.3 on 2019-01-17 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_delete_booklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=128)),
                ('auther', models.CharField(max_length=128)),
                ('format', models.CharField(max_length=64)),
                ('path', models.CharField(max_length=128)),
            ],
        ),
    ]