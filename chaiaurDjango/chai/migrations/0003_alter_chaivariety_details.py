# Generated by Django 4.2.15 on 2024-09-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_alter_chaivariety_options_chaivariety_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaivariety',
            name='details',
            field=models.TextField(default=''),
        ),
    ]
