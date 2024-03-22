# Generated by Django 5.0.3 on 2024-03-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(default='', max_length=10)),
                ('myage', models.IntegerField(default=0)),
                ('mymajor', models.CharField(default='', max_length=50)),
                ('mygit', models.CharField(default='', max_length=15)),
                ('reviewername', models.CharField(default='', max_length=10)),
                ('reviewerage', models.IntegerField(default=0)),
                ('reviewermajor', models.CharField(default='', max_length=50)),
                ('reviewergit', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
