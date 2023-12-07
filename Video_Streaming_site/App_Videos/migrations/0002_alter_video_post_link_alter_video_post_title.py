# Generated by Django 4.2.8 on 2023-12-06 17:46

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('App_Videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_post',
            name='link',
            field=embed_video.fields.EmbedVideoField(),
        ),
        migrations.AlterField(
            model_name='video_post',
            name='title',
            field=models.CharField(max_length=264),
        ),
    ]
