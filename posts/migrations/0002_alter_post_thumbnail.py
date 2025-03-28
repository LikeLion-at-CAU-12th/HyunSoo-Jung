# Generated by Django 3.2.25 on 2024-06-06 02:55

from django.db import migrations, models
import posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[posts.validators.unvalidate_file_extension], verbose_name='썸네일'),
        ),
    ]
