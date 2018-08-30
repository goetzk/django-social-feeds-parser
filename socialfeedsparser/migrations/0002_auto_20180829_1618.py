# Generated by Django 2.0.4 on 2018-08-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedsparser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='source',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn')], default=('twitter', 'Twitter'), max_length=50, verbose_name='Social media'),
        ),
    ]
