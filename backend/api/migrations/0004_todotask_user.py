# Generated by Django 5.0.6 on 2024-07-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0003_alter_todotask_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotask',
            name='user',
            field=models.CharField(default='admin', max_length=255),
        ),
    ]
