# Generated by Django 4.0.2 on 2022-02-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagedemo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
