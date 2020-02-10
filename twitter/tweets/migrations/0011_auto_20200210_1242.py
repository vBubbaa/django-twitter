# Generated by Django 2.2.7 on 2020-02-10 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0010_auto_20200209_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_liker', to=settings.AUTH_USER_MODEL),
        ),
    ]
