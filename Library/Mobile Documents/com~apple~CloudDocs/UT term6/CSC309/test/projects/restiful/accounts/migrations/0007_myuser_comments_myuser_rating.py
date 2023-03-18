# Generated by Django 4.1.6 on 2023-03-16 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='comments',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='rating',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
