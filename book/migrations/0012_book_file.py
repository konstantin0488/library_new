# Generated by Django 3.1.6 on 2021-02-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20210212_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='books'),
        ),
    ]