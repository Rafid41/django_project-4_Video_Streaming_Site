# Generated by Django 4.2.8 on 2023-12-06 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Videos', '0007_remove_video_post_cat_video_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Videos.category'),
        ),
    ]
