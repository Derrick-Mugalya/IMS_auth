# Generated by Django 2.2.5 on 2019-09-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190912_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='hasAgreed',
            field=models.BooleanField(default=False),
        ),
    ]
