# Generated by Django 3.2.4 on 2021-07-02 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_posts', '0003_postcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='owner_user',
            field=models.CharField(blank=True, default='Jon Doy', max_length=256, verbose_name='owner'),
        ),
    ]
