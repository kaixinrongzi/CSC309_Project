# Generated by Django 4.1.7 on 2023-03-20 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.myuser'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='accounts.myuser'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.myuser'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.myuser'),
        ),
    ]
