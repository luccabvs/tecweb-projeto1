# Generated by Django 3.2.7 on 2021-09-22 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_rename_category_name_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='oi', max_length=200),
        ),
    ]
