# Generated by Django 3.2.4 on 2021-07-10 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20210704_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
