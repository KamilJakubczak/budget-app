# Generated by Django 3.0.7 on 2020-08-17 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='transaction_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='api.TransactionType'),
            preserve_default=False,
        ),
    ]
