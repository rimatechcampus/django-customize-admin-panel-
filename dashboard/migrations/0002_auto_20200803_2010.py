# Generated by Django 3.0.9 on 2020-08-03 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='starter',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='last_updated',
            new_name='created_dt',
        ),
        migrations.AddField(
            model_name='topic',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topic',
            name='updated_dt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]