# Generated by Django 5.0.6 on 2024-06-13 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_todotask_due_date_alter_todotask_titel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todotask',
            old_name='titel',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='todotask',
            name='due_date',
            field=models.DateField(default=datetime.date(2024, 6, 13)),
        ),
    ]
