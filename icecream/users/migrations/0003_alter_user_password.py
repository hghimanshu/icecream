# Generated by Django 4.0 on 2023-03-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_native_name_remove_user_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
