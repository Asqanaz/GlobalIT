# Generated by Django 4.0.3 on 2022-05-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0059_facultet_hover_image_alter_facultet_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('header_image', models.FileField(blank=True, upload_to='images/Home_Page/header-images')),
                ('draft', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Mail',
                'verbose_name_plural': 'Mails',
            },
        ),
    ]
