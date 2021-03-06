# Generated by Django 3.2.4 on 2021-07-10 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_product_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='titulo',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
