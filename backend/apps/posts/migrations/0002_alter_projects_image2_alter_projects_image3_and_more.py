# Generated by Django 5.1.1 on 2024-09-09 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
