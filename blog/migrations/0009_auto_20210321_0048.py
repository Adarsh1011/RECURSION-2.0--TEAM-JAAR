# Generated by Django 3.1.4 on 2021-03-20 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20210321_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedrequest',
            name='health_centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
