# Generated by Django 4.0.3 on 2022-04-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_course_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='div_image',
            field=models.FileField(blank=True, upload_to='images/course/div-images'),
        ),
    ]
