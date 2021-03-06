# Generated by Django 4.0.3 on 2022-04-25 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_facultet_image_alter_trainer_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='option',
            new_name='option_group',
        ),
        migrations.AlterField(
            model_name='course',
            name='facultet',
            field=models.ForeignKey(default=None, help_text='klir', on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='api.facultet'),
        ),
    ]
