# Generated by Django 3.1.4 on 2021-03-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210327_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
