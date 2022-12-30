# Generated by Django 4.1.4 on 2022-12-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
