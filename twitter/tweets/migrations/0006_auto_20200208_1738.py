# Generated by Django 2.2.7 on 2020-02-09 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-created_date']},
        ),
    ]
