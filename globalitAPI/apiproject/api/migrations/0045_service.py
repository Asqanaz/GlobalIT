# Generated by Django 4.0.3 on 2022-05-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_course_students_works'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('div_image', models.FileField(blank=True, upload_to='images/service/div-images')),
                ('header_image', models.FileField(blank=True, upload_to='images/service/header-images')),
            ],
        ),
    ]
