# Generated by Django 4.0.3 on 2022-04-25 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultet',
            name='image',
            field=models.FileField(blank=True, upload_to='images/facultet'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='api.course'),
        ),
    ]
