# Generated by Django 4.0.3 on 2022-04-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_course_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.AddField(
            model_name='course',
            name='big_image',
            field=models.ImageField(blank=True, upload_to='images/course-big-images'),
        ),
        migrations.AddField(
            model_name='course',
            name='small_image',
            field=models.ImageField(blank=True, upload_to='images/course-small-images'),
        ),
    ]
