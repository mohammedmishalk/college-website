# Generated by Django 4.0.2 on 2022-04-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_leaverequest_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
