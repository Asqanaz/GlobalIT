# Generated by Django 4.0.4 on 2022-05-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_alter_curriculum_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
