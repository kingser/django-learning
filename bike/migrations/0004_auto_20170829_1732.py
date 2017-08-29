# Generated by Django 2.0 on 2017-08-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0003_remove_image_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='fileName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='filePath',
            new_name='path',
        ),
        migrations.AddField(
            model_name='image',
            name='saveDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='image',
            name='size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='type',
            field=models.CharField(default='0', max_length=15),
            preserve_default=False,
        ),
    ]
